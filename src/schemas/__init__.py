from flask_marshmallow import Marshmallow

ma = Marshmallow()

def init_schemas():
    from .todo_schema import TodoSchema