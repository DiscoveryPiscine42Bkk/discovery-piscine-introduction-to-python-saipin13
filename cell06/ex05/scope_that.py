def add_one(x):
    """Adds 1 to the parameter and returns the result."""
    x = x + 1
    return x


number = 5
print(f"Before: {number}")


add_one(number)

print(f"After: {number}")