from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta
from account.account import account, users_db
from home.home import home
from errors.errors_handling import errors_handling

app = Flask(__name__)

app.register_blueprint(account, url_prefix='/account')
app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(errors_handling, url_prefix='/error')

app.secret_key = 'hello'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.permanent_session_lifetime = timedelta(minutes=1)

users_db.init_app(app)


@app.route('/')
def main():
    if 'user' in session:
        return redirect(url_for('home.homepage'))
    else:
        return redirect(url_for('account.login'))


@app.errorhandler(404)
def invalid_route(e):
    return redirect(url_for('errors_handling.not_found_404'))


if __name__ == '__main__':
    with app.app_context():
        users_db.create_all()
    app.run(host='0.0.0.0', debug=True)
