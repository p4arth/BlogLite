# Import Initializations.
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = Flask(__name__,
            static_folder = str(os.getcwd())+ r"/static",
            template_folder = str(os.getcwd())+ r"/templates")
CORS(app, resources={r"/api": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'thisissecret'
DATABASE_PATH = "sqlite:///" + str(os.getcwd()) + "/instance/database.sqlite3"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_PATH
api = Api(app)
ma = Marshmallow(app)
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

# Import Views.
from controllers import login_controllers, post_controller, profile_controllers
from api.api_routers import *
api.add_resource(UserAPI,
                 "/api/user/<username>",
                 "/api/user/<username>/<password>")
api.add_resource(PostAPI, 
                "/api/post/<username>", 
                "/api/post/",
                "/api/post/<int:post_id>")