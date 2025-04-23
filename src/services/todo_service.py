from ..contracts.todo_dto import TodoCreateDto, TodoDto, TodoListDto
from ..repositories.todo_repository import TodoRepository
from ..models.todo_model import Todo

class TodoService:
    def __init__(self):
        self.todo_repository = TodoRepository()

    def get_all_todos(self):
        all_todos = self.todo_repository.query_all_todos()

        todos_dto = [TodoDto(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            completed=todo.completed
        ) for todo in all_todos]

        return TodoListDto(todos=todos_dto).to_dict()

    def create_todo(self, data):
        todo_details = TodoCreateDto(**data)
        todo_object = Todo(
            title=todo_details.title,
            description=todo_details.description,
            completed=False,
        )

        saved_todo = self.todo_repository.save_todo(todo_object)

        return TodoDto(
            id=saved_todo.id,
            title=saved_todo.title,
            description=saved_todo.description,
            completed=saved_todo.completed,
        ).to_dict()

    def delete_todo(self, todo_id):
        self.todo_repository.delete_todo(todo_id=todo_id)
        return

    def update_todo(self, todo_id, data):
        updated_todo = self.todo_repository.update_todo(todo_id=todo_id, data=data)
        return TodoDto(
            id=updated_todo.id,
            title=updated_todo.title,
            description=updated_todo.description,
            completed=updated_todo.completed,
        ).to_dict()

    def delete_all_todos(self):
        self.todo_repository.delete_all_todos()
        return