import tetromino as tet

# AI Class
# Creating the AI, Alice and Bob roles

class AI:
    def __init__(self, weights):

        # initialize AI by giving weights

        self.weights = weights

    def alice_play_proto(self, board, current_tetrominoes, index, coloring):

        # helper method to make a turn as Alice, returns tetromino and its score which is needed
        # to assess the best turn possible (with knowledge of look-ahead piece when trying every
        # possible outcome)
        # coloring is boolean variable, if False, we ignore the color aspect of the game,
        # if True, colorrule is enforced

        move = None
        score = float('-inf')
        current_tetromino = current_tetrominoes[index]
        for rotation in range(4):
            piece = current_tetromino.clone()
            for i in range(rotation):
                piece.rotate(board)
            while piece.moveleft(board):
                pass
            while board.valid(piece):
                __piece = piece.clone()
                while __piece.movedown(board):
                    pass
                test = board.clone()
                if coloring:
                    if not board.colorvalid(__piece):
                        piece.col += 1
                        continue
                test.place_tetromino(__piece)
                if index == 1:
                    value = (
                            - self.weights[0] * (test.aggregate_height())
                            + self.weights[1] * (test.lines())
                            - self.weights[2] * (test.holes())
                            - self.weights[3] * (test.bumpiness())
                    )
                else:
                    value = self.alice_play_proto(test, current_tetrominoes, index + 1, coloring)['score']
                if value > score:
                    score = value
                    move = piece.clone()
                piece.col += 1
        return {'tetromino': move, 'score': score}

    def alice_play(self, board, current_tetrominoes, coloring):

        # actual method for Alice's turn that only returns the tetromino

        return self.alice_play_proto(board, current_tetrominoes, 0, coloring)['tetromino']

    def bob_play(self, board, pool, current_tetromino, coloring):

        # Method for Bob's turn when he chooses the shape
        # color is random

        if len(pool.bag) == 1:
            move = pool.extractpiece(pool.bag[0])
            # if bag only has 1 piece left, turn is trivial

        else:
            comparison = []
            for tetromino_name in pool.bag:
                current_tetrominoes = [current_tetromino, tet.Tetromino(tetromino_name, pool.colors[0])]
                score = self.alice_play_proto(board, current_tetrominoes, 0, coloring)['score']
                comparison.append([tetromino_name, score])
            comparison.sort(key=lambda x: x[1])
            move = pool.extractpiece(comparison[0][0])
        return move

    def bob_play_color(self, board, pool, current_tetromino, coloring):

        # Method for Bob's turn when he chooses the color
        # shape is random


        if len(pool.colors) == 1:
            move = pool.extractcolor(pool.colors[0])
            # if bag only has 1 color left, turn is trivial

        else:
            comparison = []
            for tetromino_color in pool.colors:
                tetromino_shape = pool.bag[0]
                current_tetrominoes = [current_tetromino, tet.Tetromino(tetromino_shape, tetromino_color)]
                score = self.alice_play_proto(board, current_tetrominoes, 0, coloring)['score']
                comparison.append([tetromino_color, score])
            comparison.sort(key=lambda x: x[1])
            move = pool.extractcolor(comparison[0][0])
        return move