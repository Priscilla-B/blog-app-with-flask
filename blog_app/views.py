from flask import Blueprint, render_template, request, flash

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
def create_post():

    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        category = request.form.get('category')


    return render_template('create_post.html')