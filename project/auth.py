from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from project.models import User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.objects.filter(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user:
        flash("Oh! No!, You havn't signed up using this mail id")
        return redirect(url_for('auth.login')) # if the user doesn't exist reload the page
    elif not check_password_hash(user.password, password):
        flash("Oh! Sorry!, Your password don't match with our records")
        return redirect(url_for('auth.login')) # if the password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user,remember=remember)
    return redirect(url_for('editor.index'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.objects.filter(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email is already exists')
        return redirect(url_for('auth.signup'))
    
    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    new_user.save()
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))