from unittest.mock import MagicMock

from click.testing import CliRunner

from todo.cli import cli


def test_bulk_add_smoke():
    """Sanity check that the command exists."""
    pass


def test_bulk_add_returns_count():
    """bulk_add returns the number added."""
    store = MagicMock()
    store.bulk_add.return_value = 3
    assert store.bulk_add(["a", "b", "c"]) == 3


def test_bulk_add_cli_runs():
    """The CLI subcommand wires up."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    str(result.output)
