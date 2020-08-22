from flask import (
    Blueprint, render_template, flash,
    request, redirect, url_for, session
)

from account.account import Users
from .image_gen import generate_image

home = Blueprint('home', __name__, static_folder='static', template_folder='templates')


@home.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        # POST #

        session.pop('user', None)

        flash('You have been logged out', 'info')
        return redirect(url_for('account.login'))
    else:
        # GET #

        if 'user' in session:
            username = session.get('user')

            user_data = Users.query.filter_by(name=username).first()
            user_id = user_data.id
            caption = f'Your account number: {user_id}'

            image = generate_image(username)

            username = username.replace(' ', u'\u00a0')
            return render_template('home.html', username=username,
                                   caption=caption, image=image)
        else:
            return redirect(url_for('account.login'))
