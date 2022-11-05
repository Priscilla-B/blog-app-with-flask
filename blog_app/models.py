from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    # posts = db.relationship('Post', backref='user', passive_deletes=True)


# this table is necessary to maintain the many-to-one relationship between tags and posts
tag_post = db.Table('tag_post',
    db.Column('tag_id',db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('blog_id', db.Integer, db.ForeignKey('post.id'),primary_key=True)
)
# both columns have been set as primary keys so that a tag
# can be used only once per blog

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    author = db.orm.relationship(User)
    tags=db.relationship('Tag',secondary=tag_post,backref=db.backref('posts_associated',lazy="dynamic"))


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

