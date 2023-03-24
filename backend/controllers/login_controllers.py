from models.models import *
from models.models import Post, db, UserSchema, PostSchema
from app import app, token_required
from flask import request, jsonify
import jwt
import random
import pandas as pd
from flask_cors import cross_origin
import datetime
import numpy as np

def verify_login(username = None, password = None):
    is_user = User.query.filter_by(username = username).first()
    if not is_user:
        return False
    elif is_user is not None:
        if username == is_user.username:
            if password == is_user.password:
                return True
            return False

@app.route("/api/signup", methods = ["POST"])
@cross_origin(origin = '*', headers = ['Content-type'])
def signup_page():
    try:
        json_data = request.get_json()
        full_name = json_data["full_name"]
        username = json_data["name"]
        password = json_data["password"]
        email = json_data["email"]
        if User.query.filter_by(username = username).first() is not None:
            return jsonify({"username": username, "status": "Username is already taken"})
        else:
            new_user = User(
                full_name = full_name,
                _username = username,
                _password = password,
                email = email,
                _followers = 0,
                _posts = 0
            )
            db.session.add(new_user)
            db.session.commit()
            user_csv = pd.read_csv("./instance/metadata.csv")
            user_csv.loc[len(user_csv.index)] = [new_user.username, "", ""]
            user_csv.to_csv("./instance/metadata.csv", index = False)
            return jsonify({"username": username, "status": "New User Created"})
    except:
        return jsonify({"username": username, "status": "Unable to create user"})

@app.route("/", methods = ["POST"])
@app.route("/api/login", methods = ["POST"])
@cross_origin(origin = '*', headers = ['Content-type'])
def login_page():
    if request.method == "POST":
        json_data = request.get_json()
        try:
            username = json_data["name"]
            password = json_data["password"]
            session_verified = verify_login(username, password)
            if session_verified:
                token = jwt.encode({"username": username, 
                                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
                                    key = app.config["SECRET_KEY"])
                return jsonify({"username": username, 
                                "status": "Authenticated",
                                "auth_token": token})
            else:
                return jsonify({"username": username, "status": "Not Authenticated", "auth_token": None})
        except:
            return jsonify({"username": username, "status": "Error", "auth_token": None})

# @app.route("/api/<username>/homepage", methods = ["GET"])
# @cross_origin(origin = '*', headers = ['Content-type'])
# @token_required
# def display_user_homepage(username):
#     posts_schema = PostSchema(many = True)
#     users_schema = UserSchema(many = True)
#     recent_feed_data, user_blogs_data = user_feed_data(username)
#     posts =  db.session.query(Post).filter((Post.id != -1) & (Post.username != username)).all()
#     recommended_posts = list(np.random.choice(posts, 3))
#     users = db.session.query(User).filter(User.username != username).all()
#     if len(recent_feed_data) > 0:
#         return {"follower_blogs": posts_schema.dump(recent_feed_data),
#                 "recommendation_blogs": posts_schema.dump(recommended_posts)}
#     else:
#         return users_schema.dump(users[:5])
    
@app.route("/api/<username>/homepage", methods=["GET"])
@cross_origin(origin='*', headers=['Content-type'])
@token_required
def display_user_homepage(username):
    try:
        if not username:
            raise ValueError("Missing username parameter")
        posts_schema = PostSchema(many=True)
        users_schema = UserSchema(many=True)
        recent_feed_data, user_blogs_data = user_feed_data(username)
        if not recent_feed_data:
            users = db.session.query(User).filter(User.username != username).all()
            return users_schema.dump(users[:5]), 200
        posts = db.session.query(Post).filter((Post.id != -1) & (Post.username != username)).all()
        recommended_posts = list(np.random.choice(posts, 3))
        return {
            "follower_blogs": posts_schema.dump(recent_feed_data),
            "recommendation_blogs": posts_schema.dump(recommended_posts)
        }, 200
    except ValueError as e:
        return {"error": str(e)}, 400
    except Exception as e:
        return {"error": "An error occurred while processing your request."}, 500

@app.route("/api/<username>", methods = ["GET"])
@cross_origin(origin = '*', headers = ['Content-type'])
@token_required
def get_user_details(username):
    try:
        if not username:
            raise ValueError("Missing username parameter")
        user_schema = UserSchema()
        user = db.session.query(User).filter((User.username == username)).first()
        if not user:
            return {"message": "User not found."}, 404
        return user_schema.dump(user), 200
    except ValueError as e:
        return {"error": str(e)}, 400
    except Exception as e:
        return {"error": "An error occurred while processing your request."}, 500

def user_feed_data(username):
    following = db.session.query(Followers).filter(Followers.username == username).all()
    following = [x.follows for x in following]
    post_objs_list = []
    for follower in following:
        post_obj = db.session.query(Post).filter(Post.username == follower).all()
        for x in post_obj:
            post_objs_list.append(x)
    random.shuffle(post_objs_list)
    user_blogs = db.session.query(Post).filter(Post.username == username).all()
    return post_objs_list, user_blogs

@app.route("/api/search/", methods = ["GET"])
@cross_origin(origin = '*', headers = ['Content-type'])
def get_search_results():
    try:
        query = request.args.get("q")
        if not query:
            raise ValueError("Missing Query Parameter")
        query = "%" + query + "%"
        search_users = User.query.filter(User.username.like(query)).all()
        if not search_users:
            return {"message": "No results found."}, 200
        users_schema = UserSchema(many=True)
        return {"results": users_schema.dump(search_users)}, 200
    except ValueError as e:
        return {"error": str(e)}, 400
    except Exception as e:
        return {"error": "An error occurred while processing your request."}, 500
