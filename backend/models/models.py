from sqlite3 import Timestamp
from turtle import title
from app import db, ma

class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String, primary_key = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    full_name = db.Column(db.String, nullable = False)
    follower_count = db.Column(db.Integer)
    post_count = db.Column(db.Integer)
    pfp_link = db.Column(db.String)
    biotext = db.Column(db.String)
    
    def __init__(self, _username, _password, email, full_name, _followers = 0,
                  _posts = 0, pfp_link = None, biotext = None):
        self.username = _username
        self.password = _password
        self.full_name = full_name
        self.follower_count = _followers
        self.post_count = _posts
        self.email = email
        self.pfp_link  = pfp_link
        self.biotext = biotext

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, autoincrement = True, 
                    primary_key = True, nullable = False)
    title = db.Column(db.String, nullable = False, unique = True)
    caption = db.Column(db.String, nullable = False)
    username = db.Column(db.String, db.ForeignKey("user.username"), 
                          nullable = False)
    image_url = db.Column(db.String)
    timestamp = db.Column(db.String, nullable = False)
    def __init__(self,
                 title_ = None,
                 caption_ = None, 
                 username_ = None,
                 image_url_ = None, 
                 timestamp_ = None):
                self.title = title_
                self.caption = caption_
                self.username = username_
                self.image_url = image_url_
                self.timestamp = timestamp_

class Followers(db.Model):
    __tabelname__ = "followers"
    username = db.Column(db.String, 
                         db.ForeignKey("user.username"),  
                         primary_key = True, 
                         nullable = False)
    follows = db.Column(db.String, 
                          db.ForeignKey("user.username"),
                          primary_key = True,
                          nullable = False)
    def __init__(self, username_, follows_):
        self.username = username_
        self.follows = follows_


class UserSchema(ma.Schema):
    class Meta:
        fields = ("username", "password", "follower_count", "full_name", "post_count", "email", "pfp_link", "biotext")

class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "caption", "username", "image_url", "timestamp")

class FollowersSchema(ma.Schema):
    class Meta:
        fields = ("username", "follows")

# user_schema = UserSchema()
# users_schema = UserSchema(many=True)