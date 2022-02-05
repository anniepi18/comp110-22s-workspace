"""Wordle!"""

__author__ = "730502223"


import sys
secret: str = "codes"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(secret: str, char: str) -> bool:
    """Compares if character is found anywhere else."""
    assert len(char) == 1
    i: int = 0
    while i < len(secret):
        if char == secret[i]:
            return True
        i += 1
    return False


def emojified(secret: str, guess: str) -> str:
    """Returns string with the correct color boxes."""
    assert len(guess) == len(secret)
    result: str = ""
    i: int = 0
    while i < len(secret):
        if contains_char(secret, guess[i]) is False:
            result += WHITE_BOX
        if contains_char(secret, guess[i]) is True:
            if secret[i] == guess[i]:
                result += GREEN_BOX
            else:
                result += YELLOW_BOX
        i += 1
    return result


def input_guess(length: str) -> str:
    """Makes sure the players input is the correct length."""
    guess = str(input(f"Enter a {len(length)} character word: "))
    while len(guess) != len(length):
        guess = str(input(f"That was not {len(length)} chars! Try again: "))
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn < 7:
        print(f" === Turn {turn}/6 ===")
        guess = input_guess(secret)
        print(emojified(secret, guess))
        if secret == guess:
            print(f"You won in {turn} turns!")
            sys.exit()
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()