# Import Initializations.
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask import request, jsonify
from functools import wraps
import jwt


app = Flask(__name__,
            static_folder = str(os.getcwd())+ r"/static",
            template_folder = str(os.getcwd())+ r"/templates")
CORS(app, resources={r"/api": {"origins": "*"}})
app.config['CORS_HEADERS'] = ["Content-Type", "Authorization"]
app.config['SECRET_KEY'] = 'thisissecret'
DATABASE_PATH = "sqlite:///" + str(os.getcwd()) + "/instance/database.sqlite3"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_PATH
api = Api(app)
ma = Marshmallow(app)
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401
        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms = ['HS256'])
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401
        return f(data["username"])
    return decorated


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