import sys

def shrink(text):
    """Displays the first eight characters of the given string."""
    print(text[:8])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            shrink(arg)
    else:
        print("No parameters given.")