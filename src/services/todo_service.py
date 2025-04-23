from ..contracts.todo_dto import TodoCreateDto, TodoCreatedResponseDto
from ..repositories.todo_repository import TodoRepository
from ..models.todo_model import Todo

class TodoService:
    def __init__(self):
        self.todo_repository = TodoRepository()

    def get_all_todos(self):
        return self.todo_repository.query_all_todos()

    def create_todo(self, data):
        todo_details = TodoCreateDto(**data)
        todo_object = Todo(
            title=todo_details.title,
            description=todo_details.description,
            completed=False,
        )

        saved_todo = self.todo_repository.save_todo(todo_object)

        return TodoCreatedResponseDto(
            id=saved_todo.id,
            title=saved_todo.title,
            description=saved_todo.description,
            completed=saved_todo.completed,
        ).to_dict()

    def remove_todo(self, todo_id):
        self.todo_repository.delete_todo(todo_id=todo_id)
        return