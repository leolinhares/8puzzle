from node import Node
from collections import deque
from copy import copy, deepcopy


class Solver:
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    board_movements = {(0, 0): ('R', 'D'),
                       (0, 1): ('L', 'R', 'D'),
                       (0, 2): ('L', 'D'),
                       (1, 0): ('U', 'R', 'D'),
                       (1, 1): ('L', 'U', 'R', 'D'),
                       (1, 2): ('L', 'U', 'D'),
                       (2, 0): ('U', 'R'),
                       (2, 1): ('L', 'U', 'R'),
                       (2, 2): ('L', 'U')}

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

    @staticmethod
    def bfs():
        root = Node()
        if root.board == Solver.solution:
            return root.board
        frontier = deque()
        frontier.append(root)
        explored = set()
        while True:
            print(explored)
            # check if the queue is empty
            if not frontier:
                return 'Deu rrrrruim'
            node = frontier.popleft()
            explored.add(node.state)
            # problem being solved
            i, j = Solver.find_blank_space(node.board)
            for movement in Solver.board_movements[(i, j)]:
                child_node = Node()
                new_board = Solver.change_element_position(node.board, (i, j), movement)
                child_node.board = new_board
                if child_node not in frontier or child_node.state not in explored:
                        if child_node.board == Solver.solution:
                            return child_node
                        frontier.append(child_node)
                        explored.add(child_node.state)
