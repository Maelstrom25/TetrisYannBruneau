import random
import tetromino as tet


# Pool where Tetrominoes are drawn from

class Generator:
    def __init__(self, colorcount):

        # generates bag with tetrominoes

        self.bag = ['O', 'J', 'L', 'Z', 'S', 'T', 'I']
        self.shuffle()
        self.colorcount = colorcount
        self.colors = [(i + 1) for i in range(self.colorcount)]
        self.colorshuffle()

    def shuffle(self):

        # shuffles bag

        random.shuffle(self.bag)

    def colorshuffle(self):

        # shuffles colors

        random.shuffle(self.colors)

    def nextpiece(self):

        # yields the next tetromino, shape + color  randomized
        name, color = self.bag.pop(0), self.colors.pop(0)
        piece = tet.Tetromino(name, color)
        if not self.bag:
            self.bag = ['O', 'J', 'L', 'Z', 'S', 'T', 'I']
            self.shuffle()
        if not self.colors:
            self.colors = [(i + 1) for i in range(self.colorcount)]
            self.colorshuffle()
        return piece

    def extractpiece(self, name):

        # take out specific tetromino by shape (for Bob) - EXPERIMENT 2, 3

        self.bag.remove(name)
        color = self.colors.pop(0)
        if not self.bag:
            self.bag = ['O', 'J', 'L', 'Z', 'S', 'T', 'I']
        if not self.colors:
            self.colors = [(i + 1) for i in range(self.colorcount)]
            self.colorshuffle()
        piece = tet.Tetromino(name, color)
        return piece

    def extractcolor(self, color):

        # take out specific tetromino by color (for Bob) - EXPERIMENT 4

        self.colors.remove(color)
        name = self.bag.pop(0)
        if not self.bag:
            self.bag = ['O', 'J', 'L', 'Z', 'S', 'T', 'I']
            self.shuffle()
        if not self.colors:
            self.colors = [(i + 1) for i in range(self.colorcount)]
        piece = tet.Tetromino(name, color)
        return piece