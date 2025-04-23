from ..repositories.todo_repository import TodoRepository

class TodoService:
    def __init__(self):
        self.todo_repository = TodoRepository()

    def get_all_todos(self):
        return self.todo_repository.query_all_todos()