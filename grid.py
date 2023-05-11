# Grid Class
# Everything about board evaluation and manipulation

class Grid:
    def __init__(self, rows=22, cols=10):

        # initialize grid (matrix)

        self.rows = rows
        self.cols = cols
        self.cells = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def clone(self):

        # make a copy of the current grid to operate and test possible tetromino placements (outcomes) on
        # without changing actual grid to first see what's the best move

        clone = Grid(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                clone.cells[r][c] = self.cells[r][c]
        return clone

    def line_clear(self):

        # clear lines if full

        d = 0
        for r in range(self.rows - 1, -1, -1):
            if self.is_line(r):
                d += 1
                for c in range(self.cols):
                    self.cells[r][c] = 0
            elif d > 0:
                for c in range(self.cols):
                    self.cells[r + d][c] = self.cells[r][c]
                    self.cells[r][c] = 0
        return d

    def is_line(self, r):

        # returns True if a row (line) is full, used for line_clear mothod

        for c in range(self.cols):
            if self.cells[r][c] == 0:
                return False
        return True

    def game_over(self):

        # stops the game if the player lost (row 1 and 2 (which are not part of the game board (20x10)
        # but included as spawn point for new tetrominoes) are not empty after placing tetromino)

        for c in range(self.cols):
            if self.cells[0][c] != 0 or self.cells[1][c] != 0:
                return True
        return False

    def lines(self):

        # counts the number of full lines on current grid

        k = 0
        for r in range(self.rows):
            if self.is_line(r):
                k += 1
        return k

    def holes(self):

        # assesses number of holes on the grid

        k = 0
        for c in range(self.cols):
            block = False
            for r in range(self.rows):
                if self.cells[r][c] != 0:
                    block = True
                elif self.cells[r][c] == 0 and block:
                    k += 1
        return k

    def aggregate_height(self):

        # assesses the aggregate height, sum of all column heights

        k = 0
        for c in range(self.cols):
            k += self.height(c)
        return k

    def bumpiness(self):

        # determines how bumpy (uneven) the grid is

        k = 0
        for c in range(self.cols - 1):
            k += abs(self.height(c) - self.height(c + 1))
        return k

    def height(self, col):

        # determines height of a column

        r = 0
        while r < self.rows and self.cells[r][col] == 0:
            r += 1
        return self.rows - r

    def place_tetromino(self, tetromino):

        # places tetromino into the grid by updating grid cell values

        for i in range(tetromino.dimension):
            for j in range(tetromino.dimension):
                r = tetromino.row + i
                c = tetromino.col + j
                if tetromino.cells[i][j] != 0: #and r >= 0:
                    self.cells[r][c] = tetromino.cells[i][j]

    def valid(self, tetromino):

        # checks if current grid is valid

        for i in range(len(tetromino.cells)):
            for j in range(len(tetromino.cells[i])):
                r = tetromino.row + i
                c = tetromino.col + j
                if tetromino.cells[i][j] != 0:
                    if r < 0 or r >= self.rows:
                        return False
                    if c < 0 or c >= self.cols:
                        return False
                    if self.cells[r][c] != 0:
                        return False
        return True

    def colorvalid(self, tetromino):

        # checks if tetromino has a neighbor with the same color or not ("colorvalidity")
        # by assessing all neighboring cells and checking their color

        for i in range(tetromino.dimension):
            for j in range(tetromino.dimension):
                if tetromino.cells[i][j] != 0:
                    neighbors = []
                    if tetromino.row + i + 1 < self.rows:
                        neighbors.append(self.cells[tetromino.row + i + 1][tetromino.col + j])
                    if tetromino.col + j - 1 >= 0:
                        neighbors.append(self.cells[tetromino.row + i][tetromino.col + j - 1])
                    if tetromino.col + j + 1 < self.cols:
                        neighbors.append(self.cells[tetromino.row + i][tetromino.col + j + 1])
                    if tetromino.color in neighbors:
                        return False
        return True