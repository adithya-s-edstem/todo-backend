from dataclasses import dataclass
from typing import List

@dataclass
class TodoCreateDto:
    title: str
    description: str

@dataclass
class TodoDto:
    id: int
    title: str
    description: str
    completed: bool

    def to_dict(self):
        result = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }
        return result

@dataclass
class TodoListDto:
    todos: List[TodoDto]

    def to_dict(self):
        return [todo.to_dict() for todo in self.todos]