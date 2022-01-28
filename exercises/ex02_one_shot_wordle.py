"""One shot wordle!"""
___author___ = 730502223

secret: str = "python"
guess: str = str(input(f"What is your {len(secret)}-letter guess? "))
i: int = 0
answer: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(secret):
    guess = str(input(f"That was not {len(secret)} letters! Try again: "))

if guess == secret:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")

while i < len(secret):
    if guess[i] == secret[i]:
        answer += GREEN_BOX
    else:
        is_guess_in_secret: bool = False
        alt_index: int = 0
        while is_guess_in_secret is False and alt_index < len(secret):
            if secret[alt_index] == guess[i]:
                is_guess_in_secret = True
            else: 
                alt_index += 1    

        if is_guess_in_secret is True:
            answer += YELLOW_BOX
        else: 
            answer += WHITE_BOX
        
    i += 1
print(answer)
