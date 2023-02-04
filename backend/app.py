import os
# from flask import Flask
# from flask import render_template
# from flask import request
# from flask import redirect
# from flask_sqlalchemy import SQLAlchemy
# from controllers.login_controllers import verify_login
from app import app




if __name__ == "__main__":
    app.debug = True
    app.run()