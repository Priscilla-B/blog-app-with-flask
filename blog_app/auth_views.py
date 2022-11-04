from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User, db
from .forms import SignupForm, CreatePostForm

auth_views = Blueprint("auth_views", __name__)

@auth_views.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    form = SignupForm(request.form)
    if request.method == 'POST':
        
        if form.validate():
           
            hashed_password = generate_password_hash(form.password.data, 'sha256')
            new_user = User(
                first_name=form.first_name.data, 
                last_name=form.last_name.data, 
                email=form.email.data, 
                username=form.username.data, 
                password=hashed_password)
                 
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('Your account has been created successfully !')
            return redirect(url_for('views.home'))
    
    return render_template('sign_up.html', form=form)


@auth_views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect', category='error')
        else:
            flash('User or email doesn\'t exist', category='error')
    return render_template('login.html')


@auth_views.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out', category='success')
    return render_template('index.html')

