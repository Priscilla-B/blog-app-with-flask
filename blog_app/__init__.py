from os import path

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .views import views
from .auth_views import auth_views
from .models import User, db, migrate


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'somerandomletters'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth_views, url_prefix='/')

    with app.app_context():
        db.create_all()

    login_manager = LoginManager(app)
    login_manager.login_view = 'auth_views.login'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
