import functools
from flask import (
    Blueprint, redirect, render_template, request, session, url_for, g
)
from ahc.models import Player, Investigator
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        playername = request.form['playername']
        investigator_id = request.form['investigator_id']
        investigator = Investigator.get_by_id(investigator_id)
        player = Player.create(name=playername, investigator=investigator, location=investigator.home)
        session.clear()
        session['player_id'] = player.id
        return redirect(url_for('index'))

    current_players = Player.select(Player.investigator)
    available_investigators = Investigator.select(Investigator.id, Investigator.name).where(Investigator.id.not_in(current_players))

    return render_template('auth/login.html', investigators=available_investigators)


@bp.before_app_request
def load_logged_in_player():
    player_id = session.get('player_id')
    if player_id is None:
        g.player = None
    else:
        g.player = Player.get_by_id(player_id)


@bp.route('/logout')
def logout():
    player_id = session.get('player_id')
    if player_id is not None:
        g.player = None
        session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.player is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
