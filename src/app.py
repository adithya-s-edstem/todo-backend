from flask import Flask
from flask_migrate import Migrate
from .models import db
from .routes import register_routes
from .config import config

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.update(config.get_sqlalchemy_settings)
    db.init_app(app)
    migrate.init_app(app, db)

    register_routes(app)

    return app
