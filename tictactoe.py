from copy import deepcopy

class Board():
    # create constructor (init board class instance)
    def __init__(self, board=None):
        # define players
        self.player_1 = 'x'
        self.player_2 = 'o'
        self.empty_space = '.'

        # define board position
        self.position = {}
        
        # init (reset board)
        self.init_board()

        # create a copy of previous board state if available
        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)

    # init (reset) board
    def init_board(self):
        # loop over board rows
        for row in range(3):
            # loop over board columns
            for col in range(3):
                # set board position
                self.position[row, col] = self.empty_space

    # make move
    def make_move(self, row, col):
        # create new board instance
        board = Board(self)

        #make move
        board.position[row, col] = self.player_1

        # swap players
        (board.player_1, board.player_2) = (board.player_2, board.player_1)

        # return new board state
        return board

    # print board state
    def __str__(self):
        # define board string representation
        board_string = ''

        # loop over board rows
        for row in range(3):
            # loop over board columns
            for col in range(3):
                board_string += ' %s' % self.position[row, col]

            # add new line
            board_string += '\n'

        # prepend the player turn
        if self.player_1 == 'x':
            board_string = '\n-------------\n "x" turn to move \n-------------\n\n' + board_string
        elif self.player_1 == 'o':
            board_string = '\n-------------\n "o" turn to move \n-------------\n\n' + board_string

        # return the board string representation
        return board_string

# main driver
if __name__ == '__main__':
    # create board instance
    board = Board()

    board.position[0, 0] = 'x'
    print(board)

    board_clone = Board(board)
    print(board_clone)
