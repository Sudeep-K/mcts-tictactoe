import math
import random

# tree class definition
class TreeNode():
    # class constructor (create tree node instance)
    def __init__(self, board, parent=None):
        # init associated board state
        self.board = board

        # is node terminal flag
        if self.board.is_win() or self.board.is_draw():
            self.is_terminal = True

        # otherwise
        else:
            # we have non terminal node
            self.is_terminal = False

        # init is fully expanded flag
        self.is_fully_expanded = self.is_terminal

        # init parent node if available
        self.parent = parent

        # init the number of node visits
        self.visits = 0

        # init the total score of the node
        self.score = 0

        # init current node's children
        self.children = {}

# MCTS class definition
class MCTS():
    # search for the best move in the current position
    def search(self, inital_state):
        # create a root node
        self.root = TreeNode(inital_state, None)

        # walk through 1000 iterations
        for iteration in range(1000):
            # select a node (selection phase)
            node = self.select(self.root)

            #score current node (simulation phase)
            score = self.rollout(node.board)

            # backpropagate results
            self.backpropagate(node, score)

        # pick up the best move in the current position
        try:
            return self.get_best_move(self.root, 0)
        except:
            pass

    # select the most promising node
    def select(self, node):
        # make sure that we are dealing with non terminal nodes
        while not node.is_terminal:
            # case where node is fully expanded
            if node.is_fully_expanded:
                node = self.get_best_move(node, 2)

            # case where node is not fully expanded
            else:
                # otherwise expand the node
                return self.expand(node)
            
        # return node
        return node
    
    # expand the node
    def expand(self, node):
        # generate legal moves for the given node
        states = node.board.generate_states()

        # loop over generated states (moves)
        for state in states:
            # make sure that current state (move) is not present in child nodes
            if str(state.position) not in node.children:
                # create a new node
                new_node = TreeNode(state, node)

                # add child node to the parent's node children list (dict)
                node.children[str(state.position)] = new_node

                # case when node is fully expanded
                if len(states) == len(node.children):
                    node.is_fully_expanded = True
                
                # return newly created node
                return new_node

    # rollout (simulate) the game from the current position via making random moves until the game is finished
    def rollout(self, board):
        # make random moves for both sides until terminal state of the game is reached
        while not board.is_win():
            # try to make a move
            try:
                # make the on board
                board = random.choice(board.generate_states())
                
            # no moves available
            except:
                # return a draw score
                return 0
        
        # return score from the player "x" perspective
        if board.player_2 == 'x': return 1
        elif board.player_2 == 'o': return -1

    # backpropagate the number of visits and score up to the root node
    def backpropagate(self, node, score):
        # update nodes's up to root node
        while node is not None:
            # update node's visits
            node.visits += 1
            
            # update node's score
            node.score += score
            
            # set node to parent
            node = node.parent

    # select the best node based on the UCB1 formula
    def get_best_move(self, node, exploration_value):
        # define best score & best move
        best_score = float('-inf')
        best_moves = []

        # loop over child nodes
        for child_node in node.children.values():
            # define current player
            if child_node.board.player_2 == 'x': current_player = 1
            elif child_node.board.player_2 == 'o': current_player = -1

            # get move score using UCB1 formula
            move_score = current_player * child_node.score / child_node.visits + exploration_value * math.sqrt(math.log(node.visits) / child_node.visits)

            # better move has been found
            if move_score > best_score:
                best_score = move_score
                best_moves = [child_node]

            # found as good move as already available
            elif move_score == best_score:
                best_moves.append(child_node)

        # return random best move
        return random.choice(best_moves)

