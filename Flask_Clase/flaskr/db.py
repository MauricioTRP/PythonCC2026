import sqlite3
from datetime import datetime

import click # regitrar comandos cli de flask
from flask import current_app, g

# en variable global g
# registramos base de datos
# funciones
# revisamos usuarios

def get_db():
    """
    Si la base de datos no existe en g
    entonces creamos una.

    En cualquier caso, retornamos la base de 
    datos registrada en g.db
    """
    if 'db' not in g:
        # Creación de conexión
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e = None):
    db = g.pop('db', default= None)
    if db is not None:
        db.close()

def init_db():
    """
    iniciar el servicio cuando inicia el servidor
    o cuando se llama el comando CLI
    """
    db = get_db()

    with current_app.open_resource('schema.db') as f:
        db.executescript(f.read().decode('utf8'))

# registra comandos de CLI (command line interface)
@click.command('init-db')
def init_db_command():
    """
    Limpia la data existente y crea tablas nuevas

    Comand flask --app flaskr init-db
    """
    init_db()
    click.echo("Initialized database")

sqlite3.register_converter('timestamp', lambda v: datetime.fromisoformat(v.decode())) # registra timestamps formateados en ISO

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)