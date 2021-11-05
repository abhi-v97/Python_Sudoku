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

if __name__ == "__main__":
    print_board(board)