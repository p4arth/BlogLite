from datetime import datetime
from models.models import *
from app import app, token_required
from flask import render_template
from flask import request
from flask import redirect, jsonify
from sqlalchemy import exc
from flask_cors import cross_origin
from models.models import PostSchema

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

@app.route("/<username>/edit/post_id=<int:post_id>", methods = ["GET", "POST"])
def edit_article(username, writer_name = None, post_id = None):
    mode = "edit"
    post = get_post(
            username = username,
            writer_name = writer_name,
            post_id = post_id
        )
    if request.method  == "GET":
        return render_template("new_blog.html",
                                mode = mode,
                                username = username,
                                post_id = post.id,
                                default_text_title = post.title, 
                                defualt_text_caption = post.caption)
    elif request.method == "POST":
        now = datetime.now()
        dt_string = now.strftime(f"%d/%m/%Y %H:%M:%S")
        edited_article_title = request.form.get("article-title")
        edited_article_caption = request.form.get("article-caption")
        if not(edited_article_title) or not(edited_article_caption):
            return render_template("error.html", message = "The title or the caption cannot be empty!")
        try:
            post.title = edited_article_title
            post.caption = edited_article_caption
            post.timestamp = dt_string
            blog_img = request.form.get("blog-image")
            if blog_img:
                post.image_url = request.form.get("blog-image")
            db.session.add(post)
            db.session.commit()
        except exc.IntegrityError:
            return render_template("error.html", message = "An article with this title already exists.")
        except:
            return render_template("error.html", message = "Some error occoured. If this issue persists please contact the support.")
        return redirect(f"/{username}/homepage")

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

@app.route("/api/<username>/my-blogs")
@cross_origin(origin = '*', headers = ['Content-type'])
@token_required
def my_blogs_redir(username):
    posts_schema = PostSchema(many=True)
    posts = db.session.query(Post).filter((Post.username == username)).all()
    return posts_schema.dump(posts)

@app.route("/api/blogs/<username>")
@cross_origin(origin = '*', headers = ['Content-type'])
def user_blogs(username):
    posts_schema = PostSchema(many=True)
    posts = db.session.query(Post).filter((Post.username == username)).all()
    return posts_schema.dump(posts) 

