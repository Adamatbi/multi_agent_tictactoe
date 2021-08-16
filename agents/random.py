import numpy as np
import random

class Random:
    def __init__(self):
        pass

    def make_move(self,game):
        board = game.get_board()
        open_spots = np.where(board==0)
        rand_spot = random.randrange(len(open_spots[0]))
        return (open_spots[0][rand_spot],open_spots[1][rand_spot])