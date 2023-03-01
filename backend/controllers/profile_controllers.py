from models.models import *
from app import app, token_required
from flask import render_template
from flask import request
from flask_cors import cross_origin
from flask import redirect, jsonify
from models.models import User, db, FollowersSchema
import pandas as pd


@app.route("/api/<username>/my-profile", methods = ["GET"])
@cross_origin(origin = '*', headers = ['Content-type'])
def render_my_profile(username):
    follow_schema = FollowersSchema(many = True)
    followers_of_profile = db.session.query(Followers).filter(Followers.follows == username).all()
    user_followers = db.session.query(Followers).filter(Followers.username == username).all()
    follower_count = len(followers_of_profile)
    following_count = len(user_followers)
    user_csv = pd.read_csv("./instance/metadata.csv")
    user_csv_sub = user_csv[user_csv.username == username]
    bio_text = str(user_csv_sub["user_bio_text"].iloc[0])
    profile_picture = str(user_csv_sub["user_profile_pic_link"].iloc[0])
    return jsonify({
        "followers_count": follower_count,
        "following_count": following_count,
        "followers": follow_schema.dump(followers_of_profile),
        "following": follow_schema.dump(user_followers),
        "biotext": bio_text,
        "pfp_link": profile_picture
    })
    # if request.method == "POST":
    #     newBioText = request.form.get("newBioText")
    #     newPictureLink = request.form.get("pictureLink")
    #     user_index = user_csv_sub.index
    #     if newBioText:
    #         user_csv.loc[user_index[0],"user_bio_text"] = newBioText
    #     if newPictureLink:
    #         user_csv.loc[user_index[0],"user_profile_pic_link"] = newPictureLink
    #     user_csv.to_csv("./instance/metadata.csv", index = False)
    #     return redirect(f"/{username}/my-profile")

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
    


@app.route("/<current_user>/profile/<profile_username>", methods = ["GET", "POST"])
def render_user_profile(current_user, profile_username):
    flag = False
    followers_of_profile = db.session.query(Followers).filter(Followers.follows == profile_username).all()
    follower_count = len(followers_of_profile)
    following_of_profile = db.session.query(Followers).filter(Followers.username == profile_username).all()
    following_count = len(following_of_profile)
    
    post_list = db.session.query(Post).filter(Post.username == profile_username).all()
    follow_obj = db.session.query(Followers).filter(
                (Followers.username == current_user) & (Followers.follows == profile_username)).first()
    profile_blogs = db.session.query(Post).filter(Post.username == profile_username).all()
    follow_value = "Follow"
    if follow_obj is not None:
        follow_value = "Following"
    
    user_csv = pd.read_csv("./instance/metadata.csv")
    user_csv_sub = user_csv[user_csv.username == profile_username]
    bio_text = str(user_csv_sub["user_bio_text"].iloc[0])
    profile_picture = str(user_csv_sub["user_profile_pic_link"].iloc[0])
    if request.method == "POST":
        try:
            following_status = request.form["follow-button"]
            user = db.session.query(User).filter(User.username == profile_username).first()
            if following_status == "Following":
                follow_obj = Followers(username_ = current_user, follows_= profile_username)
                user.follower_count = user.follower_count + 1
                db.session.add(user)
                db.session.add(follow_obj)
                db.session.commit()
            else:
                user.follower_count = user.follower_count - 1
                db.session.add(user)
                db.session.delete(follow_obj)
                db.session.commit()
            followers_of_profile = db.session.query(Followers).filter(Followers.follows == profile_username).all()
            follower_count = len(followers_of_profile)
            following_of_profile = db.session.query(Followers).filter(Followers.username == profile_username).all()
            following_count = len(following_of_profile)
        except:
            return render_template("error.html", message = "Some error occoured. If this issue persists please contact the support.")
        return redirect(f"/{current_user}/profile/{profile_username}")
    else:
        return render_template("user_profile.html",
                                flag = flag,
                                default_bio_text = bio_text,
                                default_profile_picture = profile_picture,
                                follow_value = follow_value,
                                post_list = post_list,
                                profile_username = profile_username,
                                username = current_user,
                                profile_blogs = profile_blogs,
                                follower_count = follower_count,
                                following_count = following_count,
                                followers_info = followers_of_profile,
                                following_info = following_of_profile)

@app.route("/<username>/homepage/search/", methods = ["GET", "POST"])
def search_user_and_render_search_page(username):
    if request.method == "GET":
        args = request.args["searched_username"]
        tag = f"%{args}%"
        try:
            search_query = db.session.query(User).filter(User.username.like(tag)).all()
        except:
            return render_template("error.html", message = "Some error occoured. If this issue persists please contact the support.")
        return render_template("search_page.html",
                                username = username, 
                                search_results = search_query)



