from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'somerandomletters'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://test.db'

    return app