from random import shuffle, randint, sample
from sudoku_solver import valid, print_board

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def empty_board(grid):
    # print("EMPTY")
    global board
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #board = grid

    return board


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def fill(grid):

    for i in range(0, 81):
        x = i//9
        y = i % 9

        try:
            shuffle(numbers)
            for j in numbers:
                if valid(grid, j, x, y):
                    grid[x][y] = j
                elif grid[x][y] == 0:
                    empty_board(grid)
                    fill(grid)

                    return grid
        except:  # need to find a more elegant solution than just pretending the error doesn't exist
            fill(grid)


def erase(grid):

    i = randint(55, 62)
    print(81 - i)
    list = []

    while i > 0:
        x = randint(0, 8)
        y = randint(0, 8)

        if (x, y) not in list:
            list.append((x, y))
            grid[x][y] = 0
            i -= 1
        else:
            continue
        


if __name__ == "__main__":

    fill(board)

    print_board(board)
    print("--------------------- \n")
    erase(board)
    print_board(board)
