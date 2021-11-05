"""Creating a sudoku solver using the backtracking algorithm"""

s = 0
board = [
    [8, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 3, 0, 6, 0, 8],
    [0, 0, 9, 8, 0, 1, 0, 0, 6],
    [4, 1, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 4, 0, 3, 9, 5],
    [5, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 7, 0, 0, 0]
] # source: https://123sudoku.co.uk/evil-sudoku/

# print the board using enumerate
def print_board(grid):
    # i is column number, j is the entire column as a list of lists
    for i, j in enumerate(grid):
        if i % 3 == 0 and i != 0:  # if i is divisible by 3 and not zero, add columns
            print("---------------------")
        for k, l in enumerate(j):# here, j is broken into k and l, where k is a number from 0 to 9
            if k % 3 == 0 and k != 0:  # and l is the number that corresponds to k
                print("| ", end="") # So print l until loop ends, which will print 9 numbers
            print(l, end=" ")
        print()  # then this will create a new line to imitate a grid

def empty(grid):
   # for i in range(len(grid[0])):
        #for j in range(len(grid[0])):

    for i in range(0, 81): # check each cell in order from left to right
        row = i//9
        col = i%9
        if grid[row][col] == 0:
            return (row,col)
                
    return None #if no blank squares, end the backtracking loop 

def valid(grid, n, row, col):
    
    #check number does not exist in row
    for i in range(len(grid[0])):
        if grid[row][i] == n and col != i:
            return False
    #check number does not exist in column
    for i in range(len(grid[0])):
        if grid[i][col] == n and row != i:
            return False

    #check number does not exist in its square block
    rowSq = col // 3
    colSq = row // 3

    for i in range(colSq*3, colSq*3 + 3):
        for j in range(rowSq * 3, rowSq*3 + 3):
            if grid[i][j] == n and (i,j) != (row, col):
                return False

    return True

def solve(grid):
    
    find = empty(grid)
    if not find: # endgame, sudoku board is complete if this function finds no zeroes
        return True # we want to loop until it gets here
    else:
      row, col = find
        
    
    for i in range(1, 10): # using 1, 10 instead of 9 as solved sudoku doesn't have zeroes
        if valid(grid, i, row, col):
            grid[row][col] =  i
            

            if solve(grid):# loop back to start of solve function until all values are checked
                return True

            grid[row][col] =  0 #if the board isn't solved, reset to zero and try another n
    
    return False

if __name__ == "__main__":

    print_board(board)
    solve(board)
    print("---------------------")
    print_board(board)