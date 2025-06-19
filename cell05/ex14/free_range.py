import sys

def main():
    # Check for exactly 2 arguments (excluding the script name)
    if len(sys.argv) != 3:
        print("none")
        return

    try:
        # Convert arguments to integers
        start = int(sys.argv[1])
        end = int(sys.argv[2])

        # Create a list using range
        numbers = list(range(start, end))

        # Print the list
        print(numbers)

    except ValueError:
        # If arguments can't be converted to integers
        print("none")

if __name__ == "__main__":
    main()