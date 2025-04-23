from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from ..schemas.todo_schema import TodoSchema
from ..services.todo_service import TodoService

todo_blueprint = Blueprint("todo", __name__, url_prefix="/api/todos")
todo_service = TodoService()

@todo_blueprint.route("/", methods=["GET"])
def get_todos():
    todos = todo_service.get_all_todos()
    return jsonify(todos)

@todo_blueprint.route("/add", methods=["POST"])
def add_todo():
    request_data = request.get_json()
    schema = TodoSchema()
    try:
        validated_data = schema.load(request_data)
        created_todo = todo_service.create_todo(validated_data)
        return jsonify(created_todo)
    except ValidationError as e:
        return jsonify({"errors": e.messages}), 400

@todo_blueprint.route("/delete/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo_service.delete_todo(todo_id=id)
    return jsonify({"message": f"Deleted todo {id}"})

@todo_blueprint.route("/update/<int:id>", methods=["PUT"])
def update_todo(id):
    request_data = request.get_json()
    updated_todo = todo_service.update_todo(todo_id=id, data=request_data)
    return jsonify(updated_todo)

@todo_blueprint.route("/delete/all", methods=["DELETE"])
def delete_all_todos():
    todo_service.delete_all_todos()
    return jsonify({"message": "Deleted all todos"})