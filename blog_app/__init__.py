from os import path

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .views import views
from .auth_views import auth_views


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'somerandomletters'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://test.db'

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth_views, url_prefix='/')

    return app