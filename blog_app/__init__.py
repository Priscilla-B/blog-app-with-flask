import os

from flask import Flask
from flask_login import LoginManager

from .views import views
from .auth_views import auth_views
from .models import User, db, migrate
from .views import mail

from dotenv import load_dotenv
load_dotenv('.env') 


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'somerandomletters'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
    app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    db.init_app(app)
    migrate.init_app(app, db)

    mail.init_app(app)

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
