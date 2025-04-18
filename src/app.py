from flask import Flask
from utils.constants import (Settings)
from database.db_connection import Connection
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from database.db_sqlalchemy import db
import models
from flasgger import Swagger
from routes.api_routes import register_routes
from flask_cors import CORS
from database.db_intial_data import register_commands

def create_app():
    app = Flask(__name__)

    # Configuración de la app
    app.config["JWT_SECRET_KEY"] = Settings.JW_SECRET
    app.config["SQLALCHEMY_DATABASE_URI"] = Connection.URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Connection.ACTIVE_MODIFICATE

    # Extensiones
    CORS(app)
    jwt = JWTManager(app)
    db.init_app(app)
    Swagger(app)
    Migrate(app, db)

    # Comandos personalizados y rutas
    register_commands(app)
    register_routes(app)
    
    return app

app = create_app()



if __name__ == "__main__":
    app.run(host = Settings.HOST, port= Settings.PORT, debug= Settings.DEBUG)