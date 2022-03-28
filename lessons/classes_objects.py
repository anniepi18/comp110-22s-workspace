"""Example of a class and object instantiation."""


class Pizza: 
    """Models the idea of a Pizza."""
    # Attribute definitions
    size: str = "small"
    toppings: int = 3
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int):
        """Constructor definition for intialization of attributes."""
        self.size = size
        self.topppings = toppings

# function within class is called method with special parameter called self
    def price(self, tax: float) -> float:
        """Calculate the price of a pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0
        
        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0
        total *= tax
        return total 


a_pizza: Pizza = Pizza("large", 3)
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False
# Method call below
print(f"Price: ${a_pizza.price(1.05)}")
# Constructor call below
another_pizza: Pizza = Pizza("small", 0)
print(f"Price: ${another_pizza.price(1.05)}")