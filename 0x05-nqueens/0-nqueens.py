#!/usr/bin/python3
import sys

def is_valid(board, row, col, n):
    # check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # check for queens in the left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # check for queens in the right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def nqueens(board, row, n, solutions):
    if row == n:
        # all queens are placed, add solution
        solutions.append([[i, j] for i, row in enumerate(board) for j, cell in enumerate(row) if cell])
        return

    for col in range(n):
        if is_valid(board, row, col, n):
            # place queen and move to next row
            board[row][col] = 1
            nqueens(board, row + 1, n, solutions)
            # remove queen for backtracking
            board[row][col] = 0

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

def main():
    # check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # check that N is a valid integer >= 4
    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError
    except ValueError:
        print("N must be a number >= 4")
        sys.exit(1)

    board = [[0 for col in range(n)] for row in range(n)]
    solutions = []
    nqueens(board, 0, n, solutions)
    print_solutions(solutions)

if __name__ == '__main__':
    main()
