from flask import Blueprint, render_template, redirect, url_for, request

auth_views = Blueprint("auth_views", __name__)

@auth_views.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    username = request.form.get('username')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    
    return render_template('sign_up.html')

@auth_views.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    return render_template('login.html')

@auth_views.route('/logout')
def logout():
    return render_template('logout.html')

