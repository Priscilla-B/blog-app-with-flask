from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required

from .forms import CreatePostForm
from .models import Post, Tag, User, db

views = Blueprint("views", __name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template('index.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():

    form = CreatePostForm(request.form)
    user_id = current_user.get_id()
    if request.method == 'POST':
       
        new_post = Post(
            title = form.title.data,
            body = form.body.data,
            author_id = user_id,
            author = User.query.get(user_id)
        )
        
        for tag in form.tags.data:
            tag_obj = Tag.query.filter_by(name=tag).first()
            tag_obj.posts_associated.append(new_post)
            db.session.add(tag_obj)
            

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('views.home'))

    return render_template('create_post.html', form=form)


@views.route('create_post/add_tag', methods=['GET', 'POST'])
@login_required
def add_tag():

    if request.method == 'POST':
        name = request.form.get('name')
        tag_exists = Tag.query.filter_by(name=name).first()
        if tag_exists:
            flash('Tag already exists! Check select input to choose')
        else:
            new_tag = Tag(name=name)
            db.session.add(new_tag)
            db.session.commit()

        return redirect(url_for('views.create_post'))

    return render_template('add_tag.html')