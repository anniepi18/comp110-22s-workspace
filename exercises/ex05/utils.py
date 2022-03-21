"""Some utility functions!"""

__author__ = "730502223"


def only_evens(nums: list) -> list:
    """Returns only the even values in a list."""
    evens: list = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)       
    return evens


def sub(nums: list, start: int, end: int) -> list:
    """Returns a new list given the inputted start and end index."""
    end = end - 1
    new_list: list = []
    if start < 0:
        start = 0
    if end > len(nums):
        end = len(nums) - 1
    if len(nums) == 0 or start > len(nums) or end <= 0:
        return new_list
    i: int = start
    while i <= end:
        new_list.append(nums[i])
        i += 1
    return new_list


def concat(hello: list, world: list) -> list:
    """Adds the values of two lists into one new list."""
    new_list: list = []
    for num in hello:
        new_list.append(num)
    for num in world:
        new_list.append(num)
    return new_list