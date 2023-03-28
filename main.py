def is_valid(board, row, col, num):
    # Check if the number is in the current row
    if num in board[row]:
        return False

    # Check if the number is in the current column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is in the current 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def sudoku_solver(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Sudoku is solved

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if sudoku_solver(board):
                return True

            # Undo the current cell assignment and backtrack
            board[row][col] = 0

    return False  # No solution exists


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j  # row, column
    return None


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(board[i][j], end=" ")
        print()
        

if __name__ == "__main__":
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Sudoku Board:")
    print_board(sudoku_board)

    if sudoku_solver(sudoku_board):
        print("\nSolved Sudoku Board:")
        print_board(sudoku_board)
    else:
        print("\nNo solution exists.")
