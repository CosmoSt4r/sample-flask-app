from flask import (
    Blueprint, render_template, request,
    redirect, url_for, session, flash
)

from flask_sqlalchemy import SQLAlchemy
from pypasswords import *

users_db = SQLAlchemy()

account = Blueprint('account', __name__, static_folder='static', template_folder='templates')


class Users(users_db.Model):
    id = users_db.Column(users_db.Integer, primary_key=True)
    name = users_db.Column(users_db.String(24))
    password = users_db.Column(users_db.String(24))

    def __init__(self, name, password):
        self.name = name
        self.password = password


@account.route('/')
def start_page():
    if 'user' in session:
        # already logged

        return redirect(url_for('home.homepage'))
    else:
        return redirect(url_for('account.login'))


@account.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        # POST #

        username = request.form['username']
        password = request.form['password']

        found_user = Users.query.filter_by(name=username).first()
        if found_user:
            # right login

            if match_it(password, found_user.password):
                # right password
                session['user'] = username

                return redirect(url_for('home.homepage'))
            else:
                # wrong password
                flash('Incorrect login or password. Try again', 'error')
                return redirect(url_for('account.login'))
        else:
            # wrong login
            flash('Incorrect username or password. Try again', 'error')
            return render_template('login.html')
    else:
        # GET #

        if 'user' in session:
            # already logged
            return redirect(url_for('home.homepage'))
        else:
            return render_template('login.html')


@account.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == 'POST':
        # POST #

        username = request.form['username']

        if len(username) < 6 or len(username) > 24:
            # incorrect username

            flash('Username must be 6-24 characters', 'error')
            return render_template('signup.html')

        user_found = Users.query.filter_by(name=username).first()

        if user_found:
            # user already exists

            flash('This username is taken', 'error')
            return render_template('signup.html')
        else:
            if len(request.form['password']) < 6:
                # password must be 6 chars minimum

                flash('Password must be at least 6 characters', 'error')
                return render_template('signup.html')

            # hash password
            password = hash_it(request.form['password'])
            confirm_password = hash_it(request.form['confirm_password'])

            if password == confirm_password:
                new_user = Users(username, password)

                # add user to the database
                users_db.session.add(new_user)
                users_db.session.commit()
                session['user'] = username

                return redirect(url_for('home.homepage'))
            else:
                # password mismatch

                flash('The "Confirm password" confirmation doesn\'t match', 'error')
                return render_template('signup.html')
    else:
        # GET #

        if 'user' in session:
            # already logged
            return redirect(url_for('home.homepage'))
        else:
            return render_template('signup.html')
