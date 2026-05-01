import json
from pathlib import Path

from todo.model import Todo

DEFAULT_PATH = Path.home() / ".todo.json"


class JsonStorage:
    def __init__(self, path: Path = DEFAULT_PATH):
        self.path = Path(path)

    def load(self) -> list[Todo]:
        if not self.path.exists():
            return []
        data = json.loads(self.path.read_text())
        return [Todo.from_dict(d) for d in data]

    def save(self, todos: list[Todo]) -> None:
        data = [t.to_dict() for t in todos]
        self.path.write_text(json.dumps(data, indent=2))

    def next_id(self, todos: list[Todo]) -> int:
        if not todos:
            return 1
        return max(t.id for t in todos) + 1
