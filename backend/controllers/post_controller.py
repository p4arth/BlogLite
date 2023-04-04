from datetime import datetime
from models.models import *
from app import app, token_required, cache
from flask import render_template
from flask import request
from flask import jsonify, make_response
from sqlalchemy import exc
from flask_cors import cross_origin
from models.models import PostSchema
import csv
from io import StringIO

@app.route("/api/<username>/publish_new_article", methods = ["POST"])
@cross_origin(origin = '*', headers = ['Content-type'])
@token_required
def publish_post(username):
    now = datetime.now()
    json_data = request.get_json()
    dt_string = now.strftime(f"%d/%m/%Y %H:%M:%S")
    article_title = json_data["title"]
    article_caption = json_data["caption"]
    image_url = json_data["image-link"]
    post_schema = PostSchema()
    if not(article_title) or not(article_caption):
        return jsonify({
                "auth": "failed",
                "message":  "The title or the caption cannot be empty!"
            })
    try:
        user = db.session.query(User).filter(User.username == username).first()
        posts = db.session.query(Post).filter(Post.username == username).all()
        new_post = Post(
            title_ = article_title,
            caption_ = article_caption,
            username_ = username,
            image_url_ = image_url,
            timestamp_ = dt_string
        )
        db.session.add(new_post)
        user.post_count = len(list(posts)) + 1
        db.session.add(user)
        db.session.commit()
    except exc.IntegrityError:
        return jsonify({
            "auth": "failed",
            "message": "An article with this title already exists."
        })
    except:
        return jsonify({
            "auth": "failed",
            "message": "Some error occoured."
        })
    return post_schema.dump(new_post)

def get_post(username, writer_name = None, post_id = None):
    if writer_name is None:
        post = db.session.query(Post).filter(
                (Post.username == username) & (Post.id == post_id)).first()
    else:
        post = db.session.query(Post).filter(
                (Post.username == writer_name) & (Post.id == post_id)).first()
    return post

@app.route("/<username>/view/post_id=<int:post_id>")
@app.route("/<username>/view/writer_name=<writer_name>&post_id=<int:post_id>")
@app.route("/<username>/profile/view/writer_name=<writer_name>&post_id=<int:post_id>")
@cross_origin(origin = '*', headers = ['Content-type'])
def preview_article(username, writer_name = None, post_id = None):
    if request.method  == "GET":
        post = get_post(
            username = username,
            writer_name = writer_name,
            post_id = post_id
        )
        display_img_flag = True if post.image_url else False
        return render_template("display_article.html",
                                 username = username,
                                 post = post,
                                 display_img_flag = display_img_flag)

@app.route("/api/<username>/edit/post", methods = ["PUT"])
@cross_origin(origin = '*', headers = ['Content-type'])
@token_required
def edit_article(username):
    now = datetime.now()
    json_data = request.get_json()
    dt_string = now.strftime(f"%d/%m/%Y %H:%M:%S")
    post_id = json_data.get("post_id")
    article_title = json_data.get("title", "")
    article_caption = json_data.get("caption", "")
    image_url = json_data.get("image_link", "")
    post_schema = PostSchema()
    post = db.session.query(Post).filter((Post.username == username) & (Post.id == post_id)).first()
    if not(article_title) or not(article_caption):
        return jsonify({
            "auth": "Failed",
            "message": "The title or the caption cannot be empty!"
        })
    try:
        post.title = article_title
        post.caption = article_caption
        post.timestamp = dt_string
        if image_url != "":
            post.image_url = image_url
        db.session.add(post)
        db.session.commit()
    except exc.IntegrityError:
        return jsonify({
            "auth": "Failed",
            "message": "Same article already exists."
        })
    except:
        return jsonify({
            "auth": "Failed",
            "message": "Error"
        })
    return post_schema.dump(post)

@app.route("/api/<username>/delete_post", methods = ["DELETE"])
@cross_origin(origin = '*', headers = ['Content-type'])
@token_required
def delete_article(username):
    json_data = request.get_json()
    post_id = json_data["post_id"]
    try:
        post = get_post(
            username = username,
            writer_name = username,
            post_id = post_id
        )
        db.session.delete(post)
        db.session.commit()
    except exc.IntegrityError:
        return jsonify({
            "auth": "failed",
            "message": "Unable to delete article!"
        })
    except:
        return jsonify({
            "auth": "failed",
            "message": "Some error occoured."
        })
    return jsonify({
        "auth": "sucess"
    })

@cache.memoize(500)
@app.route("/api/<username>/my-blogs")
@cross_origin(origin = '*', headers = ['Content-type'])
@token_required
def my_blogs_redir(username):
    posts_schema = PostSchema(many=True)
    posts = db.session.query(Post).filter((Post.username == username)).all()
    return posts_schema.dump(posts)

@app.route("/api/get/post/<post_id>")
@cross_origin(origin = '*', headers = ['Content-type'])
def get_post_api(post_id):
    post_schema = PostSchema()
    post = db.session.query(Post).filter((Post.id == post_id)).first()
    return post_schema.dump(post)

@cache.memoize(500)
@app.route("/api/blogs/<username>")
@cross_origin(origin = '*', headers = ['Content-type'])
def user_blogs(username):
    posts_schema = PostSchema(many=True)
    posts = db.session.query(Post).filter((Post.username == username)).all()
    return posts_schema.dump(posts) 


@app.route("/api/get/blog/<username>")
@cross_origin(origin = '*', headers = ['Content-type'])
@token_required
def export_blog_csv(username):
    post_id = request.args.get('post_id')
    post = db.session.query(Post).filter((Post.id == post_id)).first()
    data = [
        ["id", "title", "caption", "username", "image_url", "timestamp"],
        [post.id, post.title, post.caption, post.username, post.image_url, post.timestamp],
    ]
    output = StringIO()
    writer = csv.writer(output)
    writer.writerows(data)
    response = make_response(output.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    response.mimetype = 'text/csv'
    return response
