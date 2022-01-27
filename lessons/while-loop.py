"""Practicing while loops"""

counter: int = 0
maximum: int = int(input("Find the squares up to: "))

while counter <= maximum:
    counter_squared = int(counter ** 2)
    print(f"The square of {counter} is {counter_squared}.")
    counter = counter + 1
print("All done!")
