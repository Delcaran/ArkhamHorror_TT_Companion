
from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        # username = request.form['username']
        session.clear()

        # session['users'] = user['id']
        return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
