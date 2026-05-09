import json
from datetime import datetime
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

    def backup(self) -> Path:
        """Write a timestamped backup of the todo file before destructive ops."""
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_path = self.path.with_suffix(f".{stamp}.bak")
        backup_path.write_text(self.path.read_text())
        return backup_path
