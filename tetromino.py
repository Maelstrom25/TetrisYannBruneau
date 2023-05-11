# Tetromino class
# Creating, moving, rotating

class Tetromino:
    def __init__(self, name, color):

        # Tetrominoes are created by giving its name (string with letter which determines shape)
        # and its color (an integer which stands for an RGB code in the Tetris class)

        self.name = name
        self.color = color
        c = self.color
        if self.name == 'O':
            self.cells = [
                [c, c],
                [c, c]
            ]
        elif self.name == 'J':
            self.cells = [
                [c, 0, 0],
                [c, c, c],
                [0, 0, 0]
            ]
        elif self.name == 'L':
            self.cells = [
                [0, 0, c],
                [c, c, c],
                [0, 0, 0]
            ]
        elif self.name == 'Z':
            self.cells = [
                [c, c, 0],
                [0, c, c],
                [0, 0, 0]
            ]
        elif self.name == 'S':
            self.cells = [
                [0, c, c],
                [c, c, 0],
                [0, 0, 0]
            ]
        elif self.name == 'T':
            self.cells = [
                [0, c, 0],
                [c, c, c],
                [0, 0, 0]
            ]
        elif self.name == 'I':
            self.cells = [
                [0, 0, 0, 0],
                [c, c, c, c],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
        self.dimension = len(self.cells) #size
        self.row = 0 #starts at top row
        self.col = (10 - self.dimension) // 2  #starts in the middle columns

    def clone(self):

        # make a copy of current tetromino (location) to try out different turns with it
        # without losing former location

        clone = Tetromino(self.name, self.color)
        clone.cells = self.cells
        clone.row = self.row
        clone.col = self.col
        return clone

    def canmoveleft(self, grid):

        # check wether moving left is possible
        # used because it is desirable to start from the left-most position and work your
        # way to the right

        for r in range(self.dimension):
            for c in range(self.dimension):
                row = self.row + r
                col = self.col + c - 1
                if self.cells[r][c] != 0:
                    if not (col >= 0 and grid.cells[row][col] == 0):
                        return False
        return True

    def canmovedown(self, grid):

        # check wether moving down is possible
        # used to determine place if tetromino should be placed into the grid

        for r in range(self.dimension):
            for c in range(self.dimension):
                row = self.row + r + 1
                col = self.col + c
                if self.cells[r][c] != 0 and row >= 0:
                    if not (row < grid.rows and grid.cells[row][col] == 0):
                        return False
        return True

    def moveleft(self, grid):

        # moving the tetromino one row to the left (if it is possible)
        # else returning False so that the AI knows it is not possible anymore

        if not self.canmoveleft(grid):
            return False
        self.col -= 1
        return True

    def movedown(self, grid):

        # moving the tetromino one column down (if its is possible)
        # else returning False so that the AI knows it is not possible anymore

        if not self.canmovedown(grid):
            return False
        self.row += 1
        return True

    def rotatecells(self):

        # rotating the tetromino (counter-clockwise)
        # but only updating the .cells, NOT the position .row + .col

        cells = [[0 for _ in range(self.dimension)] for _ in range(self.dimension)]
        if self.dimension == 2:
            return
        for i in range(self.dimension):
            for j in range(self.dimension):
                cells[i][j] = self.cells[-(j + 1)][i]

                # example for clarification (one iteration):
                # [0 1 0]     [0 0 0]
                # [1 1 0] --> [1 1 1]
                # [0 1 0]     [0 1 0]

        self.cells = cells

    def computerotateoffset(self, grid):

        # determine offset
        # needed to avoid rotation if it is NOT possible, i.e. it would rotate into an already placed
        # cell on the grid or into a wall

        piece = self.clone()
        piece.rotatecells()
        if grid.valid(piece):
            return [piece.row - self.row, piece.col - self.col]

        # Kicking
        # case where we rotate when at the left-most ir right-most row (wall)
        # we still rotate but make sure the move is legal and doesn't "leave" the grid

        inirow = piece.row
        inicol = piece.col
        for i in range(piece.dimension):
            piece.col = inicol + i
            if grid.valid(piece):
                return [piece.row - self.row, piece.col - self.col]
            for j in range(piece.dimension):
                piece.row = inirow - j
                if grid.valid(piece):
                    return [piece.row - self.row, piece.col - self.col]
            piece.row = inirow
        piece.col = inicol
        for i in range(piece.dimension):
            piece.col = inicol + i
            if grid.valid(piece):
                return [piece.row - self.row, piece.col - self.col]
            for j in range(piece.dimension):
                piece.row = inirow - j
                if grid.valid(piece):
                    return [piece.row - self.row, piece.col - self.col]
            piece.col = inicol
        piece.row = inirow
        return None

    def rotate(self, grid):

        # combining both methods above to rotate the whole tetromino (and also updates its position)

        offset = self.computerotateoffset(grid)
        if offset is not None:
            self.rotatecells()
            self.row += offset[0]
            self.col += offset[1]
