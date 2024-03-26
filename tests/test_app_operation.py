"""Test that the REPL calculator operations"""
import pytest
from app import App


def test_app_start_add(capfd, monkeypatch):
    """Test how the REPL handles an add command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['add', '4', '5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "9" in captured.out


def test_app_start_subtract(capfd, monkeypatch):
    """Test how the REPL handles an sub command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['sub', '4', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "2" in captured.out


def test_app_start_mul(capfd, monkeypatch):
    """Test how the REPL handles an mul command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['mul', '3', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "6" in captured.out


def test_app_start_div(capfd, monkeypatch):
    """Test how the REPL handles an div command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['div', '6', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "3" in captured.out
