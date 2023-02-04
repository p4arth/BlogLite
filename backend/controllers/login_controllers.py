from models.models import *
import numpy as np
from models.models import Post, db
from app import app
from flask import render_template
from flask import request, jsonify
from flask import redirect
import random
import pandas as pd
from flask_cors import CORS, cross_origin

def verify_login(username = None, password = None):
    is_user = User.query.filter_by(username = username).first()
    if not is_user:
        return False
    elif is_user is not None:
        if username == is_user.username:
            if password == is_user.password:
                return True
            return False

# @app.route("/signup", methods = ["GET", "POST"])
# def signup_page():
#     if request.method == "POST":
#         try:
#             username = request.form.get("login-username-newuser")
#             password = request.form.get("login-password-newuser")
#             if User.query.filter_by(username = username).first() is not None:
#                 return render_template("signup.html", message = "That username is already taken.")
#             else:
#                 new_user = User(
#                     _username = username,
#                     _password = password,
#                     _followers = 0,
#                     _posts = 0
#                 )
                
#                 db.session.add(new_user)
#                 db.session.commit()
#                 user_csv = pd.read_csv("./instance/metadata.csv")
#                 user_csv.loc[len(user_csv.index)] = [new_user.username, "", ""]
#                 user_csv.to_csv("./instance/metadata.csv", index = False)
#                 return redirect("/")
#         except:
#             # return render_template("error.html", message = "Some error occoured. If this issue persists please contact the support.")
#     else:
#         # return render_template("signup.html")

@app.route("/", methods = ["GET", "POST"])
@app.route("/api/login", methods = ["GET", "POST"])
@cross_origin(origin = '*', headers = ['content-type'])
def login_page():
    if request.method == "POST":
        print(request.form)
        try:
            username = request.form.get("login-username")
            password = request.form.get("login-password")
            session_verified = verify_login(username, password)
            if session_verified:
                return redirect(f"/{username}/homepage")
            else:
                return jsonify({"username": username, "status": "Not Authenticated"})
        except:
            return jsonify({"username": username, "status": "Error"})
    else:
        return render_template("login_page.html")

@app.route("/<username>/homepage")
def display_user_homepage(username):
    try:
        recent_feed_data, user_blogs_data = user_feed_data(username)
        posts =  db.session.query(Post).filter((Post.id != -1) & (Post.username != username)).all()
        recommended_posts = list(np.random.choice(posts, 3))
        users = db.session.query(User).filter(User.username != username).all()
        # return render_template("homepage.html",
        #                         username = username,
        #                         some_users = users[:5],
        #                         recent_feed_data = recent_feed_data,
        #                         user_blogs_data = user_blogs_data, 
        #                         recommended_posts = recommended_posts)
    except:
        pass
        # return render_template("error.html", message = "Some error occoured. If this issue persists please contact the support.")

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


