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
    
    # check if game is draw
    def is_draw(self):
        # loop over board squares
        for row, col in self.position:
            # empty square is available
            if self.position[row, col] == self.empty_space:
                # this is not a draw
                return False 
        
        # by default we return a draw
        return True
    
    # check if game is won
    def is_win(self):
        #############################
        # vertical square detection #
        #############################

        # loop over board columns
        for col in range(3):
            winning_sequence = []
            # check if all squares in a column are the same
            for row in range(3):
                if self.position[row, col] == self.player_2:
                    winning_sequence.append((row, col))
            
            # if there are three elements in sequence
            if len(winning_sequence) == 3:
                # return game is won
                return True
            
        #############################
        # horizontal square detection #
        #############################

        # loop over board rows
        for row in range(3):
            winning_sequence = []
            # check if all squares in a row are the same
            for col in range(3):
                if self.position[row, col] == self.player_2:
                    winning_sequence.append((row, col))
            
            # if there are three elements in sequence
            if len(winning_sequence) == 3:
                # return game is won
                return True
            
        #############################
        # first diagonal detection #
        #############################

        # init winning sequence
        winning_sequence = []

        # loop over board rows
        for row in range(3):
            # init column
            col = row

            # if found same next element in row
            if self.position[row, col] == self.player_2:
                winning_sequence.append((row, col))
            
            # if there are three elements in sequence
            if len(winning_sequence) == 3:
                # return game is won
                return True
            
        #############################
        # second diagonal detection #
        #############################

        # init winning sequence
        winning_sequence = []
        
        # loop over board rows
        for row in range(3):
            # init column
            col = 3 - row - 1

            # if found same next element in row
            if self.position[row, col] == self.player_2:
                winning_sequence.append((row, col))
            
            # if there are three elements in sequence
            if len(winning_sequence) == 3:
                # return game is won
                return True
            
    # generate legal moves to play in the current position
    def generate_states(self):
        # define states list (moves list - list of available actions to consider)
        actions = []

        # loop over board rows
        for row in range(3):
            # loop over board columns
            for col in range(3):
                # make sure that current square is empty
                if self.position[row, col] == self.empty_space:
                    # add available action to action list
                    actions.append(self.make_move(row, col))

        # return available actions
        return actions
    
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

    board.position = {
        (0, 0): 'o', (0, 1): 'x', (0, 2): 'o',
        (1, 0): 'x', (1, 1): 'o', (1, 2): 'x',
        (2, 0): 'x', (2, 1): 'o', (2, 2): 'x',
    }

    print(board)
    print('player 2: "%s"' %board.player_2)
    print('Win status', board.is_win())
