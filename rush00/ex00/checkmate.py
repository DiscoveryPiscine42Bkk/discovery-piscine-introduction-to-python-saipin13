def checkmate(board):
    size = len(board)
    king_pos = None

    
    for row in range(size):
        for col in range(size):
            if board[row][col] == 'K':
                king_pos = (row, col)
                break

    if not king_pos:
        print("Fail")
        return

    directions = {
        'P': [(-1, -1), (-1, 1)],
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)],
    }

    for row in range(size):
        for col in range(size):
            piece = board[row][col]
            if piece in directions:
                for dx, dy in directions[piece]:
                    x, y = row + dx, col + dy
                    while 0 <= x < size and 0 <= y < size:
                        if board[x][y] == 'K':
                            print("Success")
                            return
                        if board[x][y] != '.':
                            break
                        if piece == 'P': 
                            break
                        x += dx
                        y += dy

    print("Fail")