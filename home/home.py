from flask import Blueprint, render_template, request, redirect, url_for, session
from account.account import Users

home = Blueprint('home', __name__, static_folder='static', template_folder='templates')


@home.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        # POST #

        session.pop('user', None)

        return redirect(url_for('account.login'))
    else:
        # GET #

        if 'user' in session:
            username = session.get('user')

            user_data = Users.query.filter_by(name=username).first()
            user_id = user_data.id
            caption = f'Your account number: {user_id}'

            username = username.replace(' ', u'\u00a0')
            return render_template('home.html', username=username, caption=caption)
        else:
            return redirect(url_for('account.login'))
