from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_models():
    from .todo_model import Todo