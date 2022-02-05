"""Some examples of tender, loving function definitions."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string"""
    return (f"I love you, {name}")


def spread_love(to: str, n: int) -> str:
    """Generates a stirng that repeats a loving messgae n times."""
    love_note: str = ""
    i: int = 0
    while i < n: 
        love_note += love(to) + "\n"
        i += 1
    return love_note


name: str = input("Who is someone you love? ")
number: int = int(input("How many love notes do you want to send them? "))
print(spread_love(name, number))