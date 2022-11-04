from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User, db
from .forms import SignupForm

auth_views = Blueprint("auth_views", __name__)

@auth_views.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()
        if email_exists:
            flash('Email already exists.', category='error')
        elif username_exists:
            flash('Username is taken !', category='error')
        elif password1 != password2:
            flash("Passwords don't match")
        else:
            hashed_password = generate_password_hash(password1, 'sha256')
            new_user = User(
                first_name=first_name, 
                last_name=last_name, 
                email=email, 
                username=username, 
                password=hashed_password)
                 
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('Your account has been created successfully !')
            return redirect(url_for('views.home'))
    
    return render_template('sign_up.html')


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

