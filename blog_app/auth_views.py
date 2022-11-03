from flask import Blueprint, render_template, redirect, url_for

auth_views = Blueprint("auth_views", __name__)

@auth_views.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')

@auth_views.route('/login')
def login():
    return render_template('login.html')

@auth_views.route('/logout')
def logout():
    return render_template('logout.html')

