import psycopg2 #importar la libreria de postgresql
from psycopg2 import extras 

import click   #comando para crear comandos desde la terminal
from flask import current_app, g #mantienen el estado de la aplicacion
from flask.cli import with_appcontext #acceder a las variables de la aplicacion
from .schema import instructions #importar las instrucciones de la base de datos

#funcion para inicializar la base de datos
def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            dbname=current_app.config['DATABASE'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            host=current_app.config['DATABASE_HOST']
        )
        g.c = g.db.cursor(cursor_factory=extras.RealDictCursor)

    return g.db, g.c

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()  #cerrar la conexion

def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i)

    db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    