from dataclasses import dataclass
from datetime import datetime
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
    created_at: datetime

    def to_dict(self):
        result = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.timestamp(),
        }
        return result

@dataclass
class TodoListDto:
    todos: List[TodoDto]

    def to_dict(self):
        sorted_todos = sorted(self.todos, key=lambda todo: todo.created_at, reverse=True)
        return [todo.to_dict() for todo in sorted_todos]