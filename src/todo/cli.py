import click

from todo.model import Todo
from todo.storage import JsonStorage

__all__ = ["cli", "add_cmd", "list_cmd"]


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
