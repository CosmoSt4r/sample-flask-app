from flask import (
    Blueprint, render_template, request,
    redirect, url_for
)

errors_handling = Blueprint('errors_handling', __name__, static_folder='static', template_folder='templates')


@errors_handling.route('/404', methods=['GET', 'POST'])
def not_found_404():
    if request.method == 'GET':
        # GET

        return render_template('404.html')
    else:
        # POST

        return redirect(url_for('home.homepage'))
