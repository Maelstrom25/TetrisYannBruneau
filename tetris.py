import pygame
import grid
import generator as rng

# Game Visualizer Class
# Drawing the grid with pygame

class Tetris:
    def __init__(self, row_count=22, column_count=10, block_size=20):
        pygame.init()
        self.block_size = block_size
        self.height = row_count * block_size
        self.width = column_count * block_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.colors = {
            1: (255, 0, 0),   # red
            2: (0, 0, 255),   # blue
            3: (255, 255, 0), # yellow
            4: (0, 255, 0),   # green
            5: (128, 0, 128), # purple
            6: (128, 128, 0), # khaki/beige
            7: (0, 128, 128), # turqoise
            8: (128, 0, 0),   # and more....
            9: (0, 0, 128),
            10: (0, 255, 255),
            11: (0, 128, 0),
            12: (128, 255, 255),
            13: (251, 128, 255),
            14: (250, 255, 128),
            15: (255, 0, 255)
        }

    def draw_grid(self, board):

        # drawing grid (GUI)

        for i in range(board.rows):
            for j in range(board.cols):
                if board.cells[i][j] != 0:
                    color = self.colors[board.cells[i][j]]
                    pygame.draw.rect(self.screen, color,
                                     (j * self.block_size, i * self.block_size, self.block_size, self.block_size))
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255),
                                     (j * self.block_size, i * self.block_size, self.block_size, self.block_size), 1)

    def draw_tetromino(self, current_tetromino):

        # drawing tetromino (GUI)

        for i in range(current_tetromino.dimension):
            for j in range(current_tetromino.dimension):
                if current_tetromino.cells[i][j] != 0:
                    color = self.colors[current_tetromino.cells[i][j]]
                    pygame.draw.rect(self.screen, color, (
                        (current_tetromino.col + j) * self.block_size, (current_tetromino.row + i) * self.block_size, self.block_size, self.block_size))

    def draw(self, board, current_tetromino):

        # combining both methods above to draw entire GUI

        self.screen.fill((0, 0, 0))
        self.draw_grid(board)
        self.draw_tetromino(current_tetromino)
        pygame.display.flip()

    def run(self, player, colorcount, coloring, colorexp, duo, fps=1000):

        # simulation
        # duo=False => Alice plays alone, duo=True => Alice vs. Bob
        # colorexp=False => Bob chooses shape, colors random; colroexp=True => Bob chooses color, shapes are random
        # colorcount is for how many colors are used
        # coloring is a boolean which is used to choose if the colorrule is enforced or not:
        #   -> ooloring=True -> colors are important and alice cannot place tetrominoes next to cells with same color
        #   -> coloring=False -> colors are not important (regular tetris)
        # player is the AI (initialized in main.py)
        # fps is frames per second


        # tetris board is initialized
        board = grid.Grid()

        # generator/pool of tetrominoes is initialized
        pool = rng.Generator(colorcount)

        # first 2 tetrominoes are drawn randomly
        pieces = [(pool.nextpiece()), (pool.nextpiece())]


        running = True
        score = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
            self.draw(board, pieces[0])

            # Alice takes a turn, check ai.py for more info
            turn = player.alice_play(board, pieces, coloring)

            if turn is None:
                running = False
                continue

            # [piece + look-ahead piece] list is updated, look-ahead piece becomes next piece

            pieces[0] = pieces[1]

            # the following look-ahead piece is determined in following lines

            if not duo:
                # next piece is generated randomly as Alice plays alone
                pieces[1] = pool.nextpiece()

            else:
                if not colorexp:
                    # not colorexp -> Bob takes a turn, selecting tetromino shape
                    pieces[1] = player.bob_play(board, pool, pieces[0], coloring)
                else:
                    # colorexp -> Bob takes a turn, selecting tetromino color
                    pieces[1] = player.bob_play_color(board, pool, pieces[0], coloring)


            # tetromino falls down and is placed
            while turn.movedown(board):
                pass
            board.place_tetromino(turn)

            # score gets updated (if line is cleared)
            score += board.line_clear()


            # stopping condition
            if board.game_over():
                running = False
            elif score >= 200:
                score = 200
                running = False
            self.clock.tick(fps)
        #print(str(score))
        pygame.quit()
        return score
