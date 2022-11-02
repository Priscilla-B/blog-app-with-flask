from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from blog_app import create_app

app = create_app()
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column()


# @app.route('/')
# def index():
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)