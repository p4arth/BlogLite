from flask import Flask
from flask import make_response
from flask_restful import Resource, Api
from flask_restful import fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy
import json
from werkzeug.exceptions import HTTPException
from flask import make_response
from models.models import *
from datetime import datetime

user_output_fields = {
    "username": fields.String,
    "follower_count": fields.Integer,
    "post_count":  fields.Integer
}

post_output_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "caption": fields.String,
    "image_url": fields.String,
    "timestamp": fields.String,
}

post_parser = reqparse.RequestParser()
post_parser.add_argument("username")
post_parser.add_argument("password")
post_parser.add_argument("title")
post_parser.add_argument("caption")
post_parser.add_argument("image_url")

post_update_parser = reqparse.RequestParser()
post_update_parser.add_argument("username")
post_update_parser.add_argument("password")
post_update_parser.add_argument("title")
post_update_parser.add_argument("caption")
post_update_parser.add_argument("image_url")

class SchemaValidationError(HTTPException):
    def __init__(self, status_code, error_message):
        data = {"error_message": error_message}
        self.response = make_response(json.dumps(data), status_code)

class BusinessValidationError(HTTPException):
    def __init__(self, status_code, error_message):
        data = {"error_message": error_message}
        self.response = make_response(json.dumps(data), status_code)

class NotFoundError(HTTPException):
    def __init__(self, status_code):
        self.response = make_response('', status_code)

def auth(username, password):
    user = db.session.query(User).filter((User.username == username) & (User.password == password)).first()
    if user: return True
    return False

class UserAPI(Resource):
    @marshal_with(user_output_fields)
    def get(self, username):
        user = db.session.query(User).filter(User.username == username).first()
        if not user:
            raise SchemaValidationError(404, "User not found")
        else:
            return user
    
    @marshal_with(user_output_fields)
    def post(self, username, password):
        is_username_taken = db.session.query(User).filter(User.username == username).first()
        if is_username_taken:
            raise SchemaValidationError(404, "User already exists")
        new_user = User(
            _username = username,
            _password = password,
        )
        db.session.add(new_user)
        db.session.commit()
        user = db.session.query(User).filter(User.username == username).first()
        return user

    def delete(self, username, password):
        if auth(username, password):
            user = db.session.query(User).filter(User.username == username).first()
            db.session.delete(user)
            db.session.commit()
            return 200
        else:
            raise SchemaValidationError(404, "Incorrect username or password")
        
class PostAPI(Resource):
    @marshal_with(post_output_fields)
    def get(self, username):
        does_user_exist = db.session.query(User).filter(User.username == username).first()
        if not does_user_exist:
            raise SchemaValidationError(404, "User not Found")
        posts = db.session.query(Post).filter(Post.username == username).all()
        res = []
        for post in posts:
            temp = {
                "id": post.id,
                "title": post.title,
                "caption": post.caption,
                "image_url": post.image_url,
                "timestamp": post.timestamp
            }
            res.append(temp)
        return res

    @marshal_with(post_output_fields)
    def post(self):
        args = post_parser.parse_args()
        username = args.get("username", None)
        password = args.get("password", None)
        title = args.get("title", None)
        caption = args.get("caption", None)
        image_url = args.get("image_url", None)
        if (not username):
            raise BusinessValidationError(400, "Username is required")
        if (not password):
            raise BusinessValidationError(400, "Password is required")
        if (not title):
            raise BusinessValidationError(400, "Title is required")
        if (not caption):
            raise BusinessValidationError(400, "Caption is required")
        
        does_title_exist = db.session.query(Post).filter(Post.title == title).first()
        if does_title_exist:
            raise SchemaValidationError(400, "A blog with the same title already exists.")

        now = datetime.now()
        timestamp = now.strftime(f"%d/%m/%Y %H:%M:%S")
        if auth(username, password):
            new_post = Post(
                title_ = title,
                caption_= caption,
                username_= username,
                image_url_= image_url,
                timestamp_= timestamp
            )
            db.session.add(new_post)
            db.session.commit()
            return new_post
        else:
            raise SchemaValidationError(400, "Authentication failed, please check username or password.")
        
    def put(self, post_id):
        args = post_update_parser.parse_args()
        username = args.get("username", None)
        password = args.get("password", None)
        title = args.get("title", None)
        caption = args.get("caption", None)
        image_url = args.get("image_url", None)

        if (not username):
            raise BusinessValidationError(400, "Username is required")
        if (not password):
            raise BusinessValidationError(400, "Password is required")
        does_title_exist = db.session.query(Post).filter(Post.title == title).first()
        if does_title_exist:
            raise SchemaValidationError(400, "A blog with the same title already exists.")

        now = datetime.now()
        timestamp = now.strftime(f"%d/%m/%Y %H:%M:%S")
        if auth(username, password):
            post = db.session.query(Post).filter(Post.id == post_id).first()
            if title:
                post.title = title
            if caption:
                post.caption = caption
            if image_url:
                post.image_url = image_url
            post.timestamp = timestamp
            db.session.add(post)
            db.session.commit()
            return 200
        else:
            raise SchemaValidationError(400, "Authentication failed, please check username or password.")
        
    def delete(self, post_id):
        delete_update_parser = reqparse.RequestParser()
        delete_update_parser.add_argument("username")
        delete_update_parser.add_argument("password")
        args = post_update_parser.parse_args()
        username = args.get("username", None)
        password = args.get("password", None)
        if (not username):
            raise BusinessValidationError(400, "Username is required")
        if (not password):
            raise BusinessValidationError(400, "Password is required")
        if auth(username, password):
            post = db.session.query(Post).filter((Post.id == post_id) & (Post.username == username)).first()
            if not post:
                raise SchemaValidationError(404, "Post does not exist")
            db.session.delete(post)
            db.session.commit()
            return 200
        else:
            raise SchemaValidationError(400, "Authentication failed, please check username or password.")