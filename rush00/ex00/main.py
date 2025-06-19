from checkmate import checkmate

def main():
    board_str = """\
R...
.K..
..P.
...."""
    board = board_str.splitlines()
    checkmate(board)

if __name__ == "__main__":
    main()