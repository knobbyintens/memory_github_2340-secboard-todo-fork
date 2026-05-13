import click

from todo.model import Todo
from todo.storage import JsonStorage

__all__ = ["cli", "add_cmd", "list_cmd", "complete_cmd", "bulk_add_cmd"]


@click.group()
def cli() -> None:
    """A tiny command-line todo list."""


@cli.command("add")
@click.argument("title")
def add_cmd(title: str) -> None:
    """Add a new todo."""
    store = JsonStorage()
    todos = store.load()
    todo = Todo(id=store.next_id(todos), title=title)
    todos.append(todo)
    store.save(todos)
    click.echo(f"added #{todo.id}: {todo.title}")


@cli.command("list")
def list_cmd() -> None:
    """List all todos."""
    store = JsonStorage()
    todos = store.load()
    if not todos:
        click.echo("no todos yet")
        return
    for t in todos:
        mark = "x" if t.done else " "
        click.echo(f"[{mark}] #{t.id} {t.title}")


@cli.command("complete")
@click.argument("todo_id", type=int)
def complete_cmd(todo_id: int) -> None:
    """Mark a todo as done."""
    store = JsonStorage()
    todos = store.load()
    for t in todos:
        if t.id == todo_id:
            t.done = True
            store.save(todos)
            click.echo(f"completed #{todo_id}")
            return
    click.echo(f"no todo with id {todo_id}", err=True)


@cli.command("bulk-add")
@click.argument("titles", nargs=-1)
def bulk_add_cmd(titles: tuple[str, ...]) -> None:
    """Add many todos at once."""
    store = JsonStorage()
    n = store.bulk_add(list(titles))
    click.echo(f"added {n} todos")
