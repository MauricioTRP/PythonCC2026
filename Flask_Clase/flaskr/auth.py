import functools

from flask import (
    Blueprint, render_template, current_app, abort, request
)

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        # logica para obtener datos del formulario
        username = request.form['username']
        print(username)
    
    return render_template('auth/register.html')