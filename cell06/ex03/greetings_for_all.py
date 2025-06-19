def greetings(name="noble stranger"):
    """Prints a greeting if the name is a string, otherwise prints an error."""
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

# Test calls
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)