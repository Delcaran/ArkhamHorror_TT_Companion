import functools
from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for, g
)
from ahc.db import get_db
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    db = get_db()
    if request.method == 'POST':
        playername = request.form['playername']
        investigator_id = request.form['investigator_id']
        try:
            db.execute("INSERT INTO player (name, investigator_id) VALUES (?, ?)",
                       (playername, investigator_id))
            db.commit()
        except db.IntegrityError:
            error = f"Impossibile aggiungere {playername}"
        else:
            player = db.execute(
                "SELECT * FROM player WHERE name = ?", (playername,)).fetchone()
            session.clear()
            session['player_id'] = player['id']
            return redirect(url_for('index'))

        flash(error)

    available_investigators = db.execute(
        "SELECT id, name FROM investigator WHERE id NOT IN (SELECT investigator_id FROM player)").fetchall()

    return render_template('auth/login.html', investigators=available_investigators)


@bp.before_app_request
def load_logged_in_player():
    player_id = session.get('player_id')

    if player_id is None:
        g.player = None
    else:
        g.player = get_db().execute(
            'SELECT * FROM player WHERE id = ?', (player_id,)
        ).fetchone()
        g.investigator = get_db().execute(
            'SELECT * FROM investigator WHERE id = ?', (g.player["id"],)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.player is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
