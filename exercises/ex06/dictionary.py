"""Exercise 6!"""

__author__ = "730502223"


def invert(letters: dict[str, str]) -> dict[str, str]:
    """Inverts list so that keys and its key value are switched."""
    inv_dict: dict[str, str] = {}
    for key in letters:
        og_value = letters[key]
        if og_value in inv_dict:
            raise KeyError("KeyError")
        inv_dict[og_value] = key
    return inv_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Returns color that appears most frequently in a dictionary."""
    counter = {}
    if colors == {}:
        return ""
    for key, value in colors.items():
        if value not in counter:
            counter[value] = 0
        else:
            counter[value] += 1
    max: int = 0
    for item in counter:
        if counter[item] > max:
            max = counter[item]
    keys = [k for k, v in counter.items() if v == max][0]
    return keys


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of times a value occurs in a list and records in a dictionary."""
    record: dict[str, int] = {}
    for value in values:
        if value in record:
            record[value] += 1
        else:
            record[value] = 1
    return record