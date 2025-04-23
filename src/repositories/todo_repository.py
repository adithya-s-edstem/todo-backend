from . import handle_db_operation
from ..models.todo import Todo

class TodoRepository:
    def query_all_todos(self):
        todos = handle_db_operation(lambda: Todo.query.all())
        return todos
