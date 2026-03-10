from flask import Flask
import os

def create_app():
    """
    La instancia del servidor Flask
    """
    app = Flask(__name__, instance_relative_config=True) # la instancia del servidor Flask
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), # configuración para guardar la base de datos
    )

    os.makedirs(app.instance_path, exist_ok= True) # carpeta para la creación de instancias de las que depende el servidor

    # Registro de rutas
    @app.route("/hello")
    def hello():
        return "<h1>Hello world!</h1>"

    # Registro de dependencias y módulos
    # base de datos
    from . import db
    db.init_app(app=app) # registrando el package de base de datos a nuestra app

    # registro módulo autenticación
    from . import auth
    app.register_blueprint(auth.bp)

    return app