from todo.model import Todo


def test_todo_roundtrip():
    t = Todo(id=1, title="buy milk")
    data = t.to_dict()
    again = Todo.from_dict(data)
    assert again.id == t.id
    assert again.title == t.title
    assert again.done is False


def test_done_defaults_false():
    assert Todo(id=2, title="x").done is False
