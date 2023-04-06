from models.models import *
from app import app, token_required, cache
from flask import request
from flask_cors import cross_origin
from flask import jsonify
from models.models import User, db, FollowersSchema
from controllers.email_controllers import send_email_to_user


@app.route("/api/<username>/my-profile", methods = ["GET"])
@cross_origin(origin = '*', headers = ['Content-type'])
def render_my_profile(username):
    user = db.session.query(User).filter(User.username == username).first()
    follow_schema = FollowersSchema(many = True)
    followers_of_profile = db.session.query(Followers).filter(Followers.follows == username).all()
    user_followers = db.session.query(Followers).filter(Followers.username == username).all()
    follower_count = len(followers_of_profile)
    following_count = len(user_followers)
    return jsonify({
        "full_name": user.full_name,
        "followers_count": follower_count,
        "following_count": following_count,
        "followers": follow_schema.dump(followers_of_profile),
        "following": follow_schema.dump(user_followers),
        "biotext": user.biotext,
        "pfp_link": user.pfp_link,
    })

@app.route("/api/get/<username>/follows/<other_user>", methods = ["GET"])
@cross_origin(origin = '*', headers = ['Content-type'])
def get_user_followers(username, other_user):
    isFollowing = db.session.query(Followers).filter(
        (Followers.username == username) & (Followers.follows == other_user)
    ).first()
    return jsonify({
        "following": True if isFollowing else False,
    })

@app.route("/api/<username>/follow", methods = ["POST", "DELETE"])
@cross_origin(origin = '*', headers = ['Content-type'])
@token_required
def follow_func(username):
    data = request.get_json()
    if request.method == "POST":
        has_to_follow = data["has_to_follow"]
        follow_obj = Followers(
            username_= username,
            follows_= has_to_follow
        )
        db.session.add(follow_obj)
        db.session.commit()
        return jsonify({
            'auth': "success"
        })
    elif request.method == "DELETE":
        has_to_unfollow = data["has_to_unfollow"]
        follower_Obj = db.session.query(Followers).filter(
            (Followers.username == username) & (Followers.follows == has_to_unfollow)
        ).first()
        db.session.delete(follower_Obj)
        db.session.commit()
        return jsonify({
            'auth': "DELETED"
        })

@app.route("/api/get/profile_picture/<username>", methods = ["GET"])
@cross_origin(origin = '*', headers = ['Content-type'])
def get_user_profile(username):
    user = db.session.query(User).filter(User.username == username).first()
    return jsonify({
        "link": user.pfp_link,
    })

@app.route("/api/profile_change/<username>", methods = ["POST"])
@cross_origin(origin = '*', headers = ['Content-type'])
@token_required
def change_user_profile(username):
    user = db.session.query(User).filter(User.username == username).first()
    data = request.get_json()
    new_pfp_link = data.get("new_pfp", None)
    new_bio_text = data.get("new_bio", None)
    if new_pfp_link:
        user.pfp_link = new_pfp_link
    if new_bio_text:
        user.biotext = new_bio_text
    db.session.add(user)
    db.session.commit()
    return jsonify({
        "auth": "success",
    })