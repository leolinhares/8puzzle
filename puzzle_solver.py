from node import Node
from collections import deque
from copy import copy, deepcopy


class Solver:
    def __init__(self):
        self.solution = Node([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    board_movements = {(0, 0): ('R', 'D'),
                       (0, 1): ('L', 'R', 'D'),
                       (0, 2): ('L', 'D'),
                       (1, 0): ('U', 'R', 'D'),
                       (1, 1): ('L', 'U', 'R', 'D'),
                       (1, 2): ('L', 'U', 'D'),
                       (2, 0): ('U', 'R'),
                       (2, 1): ('L', 'U', 'R'),
                       (2, 2): ('L', 'U')}

    empty_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    @staticmethod
    def find_blank_space(board):
        """
        :param board: matrix[3][3]
        :return: a tuple with the position of the element zero.
        """
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == 0:
                    return i, j

    @staticmethod
    def change_element_position(board, zero_position, movement):
        """
        :param board: matrix[3][3]
        :param zero_position: tuple with the position of element zero
        :param movement: with move will be executed
        :return: a new board after the change of an element's position
        """
        new_board = deepcopy(board)
        i, j = zero_position
        if movement == 'L' and j > 0:
            aux = new_board[i][j - 1]
            new_board[i][j - 1] = 0
            new_board[i][j] = aux
        elif movement == 'U' and i > 0:
            aux = new_board[i - 1][j]
            new_board[i - 1][j] = 0
            new_board[i][j] = aux
        elif movement == 'R' and j >= 0:
            aux = new_board[i][j + 1]
            new_board[i][j + 1] = 0
            new_board[i][j] = aux
        elif movement == 'D' and i >= 0:
            aux = new_board[i + 1][j]
            new_board[i + 1][j] = 0
            new_board[i][j] = aux
        else:
            pass
        return new_board

    def bfs(self):
        root = Node()

        if root.state == self.solution.state:
            return root.board

        frontier = deque()  # Creating a FIFO (queue)
        frontier.append(root)  # Adding the root to the frontier (which will be following explored)
        explored = set()  # Creating an empty set to store the explored notes
        explored.add(root.state)
        # a = 0
        # checking if the queue is empty
        while frontier:
            node = frontier.pop()  # Removing the first element of the queue (will be explored)

            if node.state == self.solution.state:
                return node

            # problem being solved
            i, j = Solver.find_blank_space(node.board)  # Find the tuple (i, j) with the zero location
            movements = Solver.board_movements[(i, j)]
            for movement in movements:

                # Creating the new board for the child node based on one of the allowed movements
                new_board = Solver.change_element_position(node.board, (i, j), movement)
                child_node = Node(Solver.empty_board)
                child_node.board = new_board

                if child_node.state not in explored:
                    frontier.appendleft(child_node)
                    explored.add(child_node.state)
