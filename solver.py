# this is a sudoku solver

def solve(board):
    find = find_empty(board)
    if not find: #if there is no more empty space, meaning we have found the solution
        return True
    else:
        row, col = find

    for i in range(1, 10): # Iterate i from 1 to 9
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

     return False   