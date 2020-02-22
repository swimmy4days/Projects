grid = [
    [0, 0, 3, 0, 7, 2, 0, 0, 8],
    [0, 0, 0, 0, 1, 5, 3, 6, 0],
    [0, 8, 0, 0, 0, 0, 7, 0, 0],
    [4, 5, 0, 3, 9, 0, 0, 0, 2],
    [0, 3, 2, 0, 4, 0, 6, 9, 0],
    [7, 0, 0, 0, 2, 1, 0, 3, 5],
    [0, 0, 7, 0, 0, 0, 0, 5, 0],
    [0, 6, 1, 2, 5, 0, 0, 0, 0],
    [9, 0, 0, 7, 3, 0, 0, 0, 0]
]


def solve(sudoku):
    """
    A simple sudoku solver using backtraking.
        :param sudoku: The two-dimensional array, 9 long array of 9 long arrays of ints, from 0-9. 0 is empty.
    """
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n, sudoku):
                        sudoku[y][x] = n
                        solve(sudoku)
                        sudoku[y][x] = 0
                return

    for x in range(9):
        for y in range(9):
            print(grid[x][y], end=' ')
        print()

    input("There might be other sulotions...\n")


def possible(y, x, n, maze):
    """
    A function that checks if a number is in the same block, row or colmun that, if it is returing False, else True.
        :param y: The Y value of the cell.
        :param x: The X value of the cell.
        :param n: The wanted number to be searched.
        :param maze: The 9X9 sudoku array.
    """
    for i in range(9):
        if maze[y][i] == n:
            return False
        if maze[i][x] == n:
            return False

    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if maze[y0 + i][x0 + j] == n:
                return False
    return True


if __name__ == "__main__":
    global gird
    solve(grid)
