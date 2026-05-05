from unittest.mock import patch

from click.testing import CliRunner

from todo.cli import cli


def test_add():
    with patch("todo.cli.JsonStorage") as mock_store_cls:
        store = mock_store_cls.return_value
        store.load.return_value = []
        store.next_id.return_value = 1

        runner = CliRunner()
        result = runner.invoke(cli, ["add", "buy milk"])

        assert result.exit_code == 0
        assert "added #1: buy milk" in result.output
        store.save.assert_called_once()


def test_list_empty():
    with patch("todo.cli.JsonStorage") as mock_store_cls:
        mock_store_cls.return_value.load.return_value = []
        runner = CliRunner()
        result = runner.invoke(cli, ["list"])
        assert "no todos yet" in result.output
