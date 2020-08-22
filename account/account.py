from flask import Blueprint, render_template, request, redirect, url_for, session
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


@account.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        # POST #

        username = request.form['username']
        password = request.form['password']

        found_user = Users.query.filter_by(name=username).first()
        if found_user:
            if match_it(password, found_user.password):
                session['user'] = username

                return redirect(url_for('home.homepage'))
            else:
                # password doesn't match
                return render_template('login.html')
        else:
            # user isn't existing
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
        if len(request.form['password']) < 6 or ' ' in request.form['password']:
            # password can't contain spacings and must be 6 chars minimum
            return render_template('signup.html')

        password = hash_it(request.form['password'])
        confirm_password = hash_it(request.form['confirm_password'])

        user_found = Users.query.filter_by(name=username).first()

        if user_found:
            return render_template('login.html')  # already exists
        else:
            if password == confirm_password:
                new_user = Users(username, password)

                users_db.session.add(new_user)
                users_db.session.commit()
                session['user'] = username
                return redirect(url_for('home.homepage'))
            else:
                # passwords don't match
                return render_template('signup.html')
    else:
        # GET #

        if 'user' in session:
            # already logged
            return redirect(url_for('home.homepage'))
        else:
            return render_template('signup.html')
