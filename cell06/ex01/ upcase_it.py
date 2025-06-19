def upcase_it(text):
    """Converts the input string to uppercase."""
    return text.upper()


if __name__ == "__main__":
    test_string = "hello"
    result = upcase_it(test_string)
    print(f"Original: {test_string}")
    print(f"Uppercase: {result}")