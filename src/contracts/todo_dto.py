from dataclasses import dataclass

@dataclass
class TodoCreateDto:
    title: str
    description: str

@dataclass
class TodoCreatedResponseDto:
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