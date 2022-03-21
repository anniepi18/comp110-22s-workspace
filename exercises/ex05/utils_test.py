"""Tests for utils function."""

from exercises.ex05.utils import sub, only_evens, concat


def test_only_evens_empty() -> None:
    """Makes sure an empty list returns and empty list."""
    nums = []
    assert only_evens(nums) == []


def test_only_evens_with_nums() -> None:
    """Tests the function works with a simple list."""
    nums = [1, 2, 3, 4, 5]
    assert only_evens(nums) == [2, 4]


def test_only_evens_with_none() -> None:
    """Makes sure a list with all odds returns empty."""
    nums = [1, 3, 5, 7, 9]
    assert only_evens(nums) == []


def test_sub_empty_list() -> None:
    """Tests that an empty lists returns empty."""
    nums = []
    assert sub(nums, 0, 5) == []


def test_sub_bad_start() -> None:
    """Tests that a negative start gets rewritten at 0."""
    nums = [0, 1, 2, 3, 4]
    assert sub(nums, -2, 4) == [0, 1, 2, 3]


def test_sub_bad_end() -> None:
    """Tests that an end larger than length gets rewritten as length - 1."""
    nums = [0, 1, 2, 3, 4]
    assert sub(nums, 1, 8) == [1, 2, 3, 4]


def test_concat_empty_hello() -> None:
    """Tests the function works with one list empty."""
    hello = []
    world = [1, 2, 3]
    assert concat(hello, world) == [1, 2, 3]


def test_concat() -> None:
    """Tests the function works with two simple lists."""
    hello = [1, 2, 3]
    world = [4, 5, 6]
    assert concat(hello, world) == [1, 2, 3, 4, 5, 6]


def test_concat_empty_both() -> None:
    """Tests that two empty lists return empty."""
    hello = []
    world = []
    assert concat(hello, world) == []