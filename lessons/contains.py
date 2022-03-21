"""Example of writing a function to search a list"""

# Define a function named contains with parameters 
# needle: the str we're searching for and haystack: the list of str values we are searching through
# Algorithm: for each item in haystack, if equal to needle, return True, if after all are checked
# and needle not found, return False
def main() -> None:
    guess: str = input("What is the code word? ")
    possible_answers: list = ["pokemon", "wordle"]
    if contains(guess, possible_answers):
        print("We're letting you in the secret club...")
    else:
        print("Go back to Davis.")


def contains(needle: str, haystack: list) -> bool: 
    """Sees if needle is found in haystack."""
    for item in haystack:
        if item == needle:
            return True
    return False


if __name__ == "__main__":
    main()