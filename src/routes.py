from src.controllers.todo_controller import todo_blueprint

def register_routes(app):
    app.register_blueprint(todo_blueprint)