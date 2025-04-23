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

    def delete_todo(self, todo_id):
        def delete_operation():
            todo = Todo.query.filter_by(id=todo_id).first()
            if todo is None:
                raise ValueError(f"Todo with id {todo_id} does not exist.")
            db.session.delete(todo)
            db.session.commit()

        return handle_db_operation(delete_operation)

    def update_todo(self, todo_id, data):
        def update_operation():
            existing_todo = Todo.query.filter_by(id=todo_id).first()
            if existing_todo is None:
                raise ValueError(f"Todo with id {todo_id} does not exist.")
            for attr, value in data.items():
                if attr != 'id':
                    setattr(existing_todo, attr, value)
            db.session.add(existing_todo)
            db.session.commit()
            db.session.refresh(existing_todo)
            return existing_todo
        return handle_db_operation(update_operation)