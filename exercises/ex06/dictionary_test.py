"""Test file for exercise 6!"""

__author__ = "730502223"

from dictionary import invert, favorite_color, count


def test_invert_nums() -> None:
    """Makes sure function works normally."""
    letters = {"Hello": "1", "World": "2", "Annie": "3"}
    assert invert(letters) == {"1": "Hello", "2": "World", "3": "Annie"}


def test_invert_empty() -> None:
    """Tests that an empty input results in an empty output."""
    letters: dict[str, str] = {}
    assert invert(letters) == {}


def test_invert_reg() -> None:
    """Tests that with duplicate keys, the values will combine into that key."""
    letters = {"Hello": "World", "World": "Hello", "Annie": "Pi"}   
    assert invert(letters) == {"World": "Hello", "Hello": "World", "Pi": "Annie"}


def test_favorite_color_tie() -> None:
    """Tests that one is returned if two have the same frequency."""
    colors = {"Annie": "Purple", "Evan": "Purple", "Christina": "Blue", "Joshi": "Blue"}
    assert favorite_color(colors) == "Purple"


def test_favorite_color_empty() -> None:
    """Tests that an empty dictonary doesn't return anything."""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ""


def test_favorite_color_reg() -> None:
    """Asserts the function works under normal circumstances."""
    colors = {"Annie": "Purple", "Evan": "Purple", "Christina": "Orange", "Joshi": "Blue"}
    assert favorite_color(colors) == "Purple"


def test_count_reg() -> None:
    """Asserts that the function works under normal circumstances."""
    values = ["a", "a", "a", "b", "c"]
    assert count(values) == {"a": 3, "b": 1, "c": 1}


def test_count_empty() -> None:
    """Asserts that an empty input results in an empty dictonary."""
    values: list[str] = []
    assert count(values) == {}


def test_count_nums() -> None:
    """Asserts that a list with nums still returns properly."""
    values = ["1", "3", "3", "1", "1", "1", "2"]
    assert count(values) == {'1': 4, '2': 1, '3': 2}