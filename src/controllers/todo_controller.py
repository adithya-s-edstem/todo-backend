from flask import Blueprint, jsonify
from ..services.todo_service import TodoService

todo_blueprint = Blueprint("todo", __name__, url_prefix="/api/todos")
todo_service = TodoService()


@todo_blueprint.route("/", methods=["GET"])
def get_todos():
    todos = todo_service.get_all_todos()
    return jsonify(todos)
