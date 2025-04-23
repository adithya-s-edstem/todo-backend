from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from .models import db, init_models
from .routes import register_routes
from .config import config
from .schemas import ma, init_schemas

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.update(config.get_sqlalchemy_settings)
    db.init_app(app)
    ma.init_app(app)

    migrate.init_app(app, db)

    init_models()
    init_schemas()

    register_routes(app)

    return app
