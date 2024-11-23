import os

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config

    # Reemplaza con tus configuraciones de base de datos reales
    app.config['DATABASE'] = 'ejemplo'
    app.config['DATABASE_USER'] = 'ejemplo'
    app.config['DATABASE_PASSWORD'] = 'ejemplo'  # Asegúrate de que esté configurada
    app.config['DATABASE_HOST'] = 'ejemplo'  # o tu host real

    from . import db

    db.init_app(app)
    
    from . import auth
    from . import todo


    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    @app.route('/hola')
    def hola():
        return 'Chanchito Feliz'
    
    return app
