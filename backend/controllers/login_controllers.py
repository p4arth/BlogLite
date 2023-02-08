from models.models import *
import numpy as np
from models.models import Post, db, UserSchema, PostSchema
from app import app
from flask import request, jsonify
# from flask import redirect
import jwt
from functools import wraps
import random
import pandas as pd
from flask_cors import cross_origin
import datetime

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401
        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(username = data["username"]).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

def verify_login(username = None, password = None):
    is_user = User.query.filter_by(username = username).first()
    if not is_user:
        return False
    elif is_user is not None:
        if username == is_user.username:
            if password == is_user.password:
                return True
            return False

# @app.route("/", methods = ["POST"])
@app.route("/api/signup", methods = ["POST"])
@cross_origin(origin = '*', headers = ['Content-type'])
def signup_page():
    try:
        json_data = request.get_json()
        username = json_data["name"]
        password = json_data["password"]
        if User.query.filter_by(username = username).first() is not None:
            return jsonify({"username": username, "status": "Username is already taken"})
        else:
            new_user = User(
                _username = username,
                _password = password,
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
                print(token)
                return jsonify({"username": username, 
                                "status": "Authenticated",
                                "auth_token": token})
            else:
                return jsonify({"username": username, "status": "Not Authenticated", "auth_token": None})
        except:
            return jsonify({"username": username, "status": "Error", "auth_token": None})

@app.route("/api/<username>/homepage", methods = ["GET"])
@cross_origin(origin = '*', headers = ['Content-type'])
def display_user_homepage(username):
    try:
        print("-"*50)
        posts_schema = PostSchema(many = True)
        users_schema = UserSchema(many = True)
        recent_feed_data, user_blogs_data = user_feed_data(username)
        posts =  db.session.query(Post).filter((Post.id != -1) & (Post.username != username)).all()
        # recommended_posts = list(np.random.choice(posts, 3))
        users = db.session.query(User).filter(User.username != username).all()
        if len(recent_feed_data) > 0:
            return posts_schema.dump(recent_feed_data)
        else:
            return users_schema.dump(users[:5])
        # return render_template("homepage.html",
        #                         username = username,
        #                         some_users = users[:5],
        #                         recent_feed_data = recent_feed_data,
        #                         user_blogs_data = user_blogs_data, 
        #                         recommended_posts = recommended_posts)
    except:
        pass
        # return render_template("error.html", message = "Some error occoured. If this issue persists please contact the support.")

@app.route("/api/<username>", methods = ["GET"])
@cross_origin(origin = '*', headers = ['Content-type'])
def get_user_details(username):
    user_schema = UserSchema()
    user = db.session.query(User).filter((User.username == username)).first()
    return user_schema.dump(user)

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


