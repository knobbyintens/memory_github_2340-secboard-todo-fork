from pathlib import Path

from todo.model import Todo
from todo.storage import JsonStorage


def test_save_and_load(tmp_path: Path):
    store = JsonStorage(path=tmp_path / "todos.json")
    todos = [Todo(id=1, title="a"), Todo(id=2, title="b", done=True)]
    store.save(todos)
    loaded = store.load()
    assert len(loaded) == 2
    assert loaded[0].title == "a"
    assert loaded[1].done is True


def test_load_missing_returns_empty(tmp_path: Path):
    store = JsonStorage(path=tmp_path / "nope.json")
    assert store.load() == []


def test_next_id(tmp_path: Path):
    store = JsonStorage(path=tmp_path / "todos.json")
    assert store.next_id([]) == 1
    assert store.next_id([Todo(id=1, title="x"), Todo(id=4, title="y")]) == 5
