def is_valid_sudoku(board):
    N = len(board)  # Size of the board
    sqrt_N = int(N ** 0.5)  # Size of the sub-boxes

    # Check rows
    for row in board:
        if not _is_valid_sequence(row, N):
            return False

    # Check columns
    for col in range(N):
        if not _is_valid_sequence([row[col] for row in board], N):
            return False

    # Check sub-boxes (sqrt_N x sqrt_N)
    for row_start in range(0, N, sqrt_N):
        for col_start in range(0, N, sqrt_N):
            subbox = [board[row][col] 
                      for row in range(row_start, row_start + sqrt_N) 
                      for col in range(col_start, col_start + sqrt_N)]
            if not _is_valid_sequence(subbox, N):
                return False

    return True  # If all checks pass, the Sudoku is valid

def _is_valid_sequence(seq, N):
    """Helper function to check if a sequence has numbers 1 to N without repeats"""
    seen = set()
    return len(seq) == N and all(num in seen.add(num) for num in seq if num) 

# Example usage with a Sudoku puzzle
board = [
    [7, 8, 4, 1, 5, 9, 3, 2, 6],
    [5, 3, 9, 6, 7, 2, 8, 4, 1],
    [6, 1, 2, 4, 3, 8, 7, 5, 9],
    [9, 2, 8, 7, 1, 5, 4, 6, 3],
    [3, 5, 7, 8, 4, 6, 1, 9, 2],
    [4, 6, 1, 9, 2, 3, 5, 8, 7],
    [8, 7, 6, 3, 9, 1, 2, 5, 4],
    [2, 4, 3, 5, 6, 7, 9, 1, 8],
    [1, 9, 5, 2, 8, 4, 6, 3, 7]
]

if is_valid_sudoku(board):
    print("Valid Sudoku")
else:
    print("Invalid Sudoku")
