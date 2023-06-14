from copy import deepcopy

class Board():
    # create constructor (init board class instance)
    def __init__(self, board=None):
        # define players
        self.player_1 = 'x'
        self.player_2 = 'o'

        # define board position
        self.position = {}
        
        # init (reset board)
        self.empty_space = '.'

        # create a copy of previous board state if available
        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)

# main driver
if __name__ == '__main__':
    # create board instance
    board = Board()

    print(board.__dict__)
