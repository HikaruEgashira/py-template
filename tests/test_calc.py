"""Tests for calc.py."""

from src import calc


def test_add() -> None:
    """Test the add function."""
    assert calc.add(1, 2) == 3
