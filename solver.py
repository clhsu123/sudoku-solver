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

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and i!=pos.[1]:
            return False
    
    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and i!=pos[0]:
            return False

    # Check box
    row_box = pos[0] // 3
    col_box = pos[1] // 3

    for i in range(row_box*3, row_box*3+3):
        for j in range(col_box*3, col_box*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True

        

      