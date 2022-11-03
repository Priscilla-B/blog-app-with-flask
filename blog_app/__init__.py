from os import path

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .views import views
from .auth_views import auth_views

db = SQLAlchemy()
DB_NAME = 'blog.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'somerandomletters'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth_views, url_prefix='/')

    create_database(app)

    return app

def create_database(app):
    if not path.exists('blog_app/'+DB_NAME):
        db.create_all(app=app)
