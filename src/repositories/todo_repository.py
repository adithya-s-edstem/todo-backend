from . import handle_db_operation
from ..models.todo_model import Todo
from ..models import db

class TodoRepository:
    def query_all_todos(self):
        todos = handle_db_operation(lambda: Todo.query.all())
        return todos

    def save_todo(self, todo):
        def save_operation():
            db.session.add(todo)
            db.session.commit()
            db.session.refresh(todo)
            return todo

        return handle_db_operation(save_operation)