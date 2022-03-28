"""Examples of default parameters."""


def add(x: int, y: int = 0, z: int = 0) -> int:
    """Can now call function without second parameter because it's set to some value by default."""
    """However, every param after that also have to be default. This can be used in constructors and methods as well."""
    return x + y


print(add(1, 2))
print(add(2))
print(add(1, 2, 3))