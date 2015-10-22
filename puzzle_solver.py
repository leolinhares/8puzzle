from node import Node
from copy import deepcopy
from collections import deque


class Solver:
    solution = Node([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

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
    def swap(board, parent_coordinates, child_coordinates):
        i, j = child_coordinates
        a, b = parent_coordinates
        copy_board = [elem[:] for elem in board]

        aux = copy_board[i][j]
        copy_board[i][j] = 0  # copy_board[a][b]
        copy_board[a][b] = aux

        return copy_board

    @staticmethod
    def generate_children(parent):
        children = []

        parent_i, parent_j = Solver.find_blank_space(parent.board)
        movements = Solver.board_movements[(parent_i, parent_j)]

        for movement in movements:
            child_i, child_j = parent_i, parent_j
            if movement == 'L':
                child_i, child_j = parent_i, parent_j - 1
            elif movement == 'U':
                child_i, child_j = parent_i - 1, parent_j
            elif movement == 'R':
                child_i, child_j = parent_i, parent_j + 1
            elif movement == 'D':
                child_i, child_j = parent_i + 1, parent_j
            else:
                pass
            child_board = Solver.swap(parent.board, (parent_i, parent_j), (child_i, child_j))
            child = Node(child_board)
            child.parent = parent
            children.append(child)
        return children

    @staticmethod
    def breadth_first_search():
        root = Node()
        visited, queue = set(), deque([root])
        while queue:
            node = queue.pop()
            if node.state in visited:
                continue

            if node.state == Solver.solution.state:
                return node

            visited.add(node.state)

            for child in Solver.generate_children(node):
                if child.state not in visited:
                    if child.state == Solver.solution.state:
                        return child
                    # # o pai da raiz nao existe
                    # if node.parent is None:
                    #     queue.appendleft(child)
                    # # filhos nao podem ser iguais ao avo
                    # elif child.state != node.parent.state:
                    #     queue.appendleft(child)
                    else:
                        queue.appendleft(child)
        return "Error"

    # @staticmethod
    # def path(solution_node, root):
    #     path = []
    #     node = solution_node
    #     while node.parent.state != root.state:
    #         path.append(node)
    #         node = node.parent
    #     path.append(root)
    #     return path

    # @staticmethod
    # def change_element_position(board, zero_position, movement):
    #     """
    #     :param board: matrix[3][3]
    #     :param zero_position: tuple with the position of element zero
    #     :param movement: with move will be executed
    #     :return: a new board after the change of an element's position
    #     """
    #     new_board = deepcopy(board)
    #     i, j = zero_position
    #     if movement == 'L' and j > 0:
    #         aux = new_board[i][j - 1]
    #         new_board[i][j - 1] = 0
    #         new_board[i][j] = aux
    #     elif movement == 'U' and i > 0:
    #         aux = new_board[i - 1][j]
    #         new_board[i - 1][j] = 0
    #         new_board[i][j] = aux
    #     elif movement == 'R' and j >= 0:
    #         aux = new_board[i][j + 1]
    #         new_board[i][j + 1] = 0
    #         new_board[i][j] = aux
    #     elif movement == 'D' and i >= 0:
    #         aux = new_board[i + 1][j]
    #         new_board[i + 1][j] = 0
    #         new_board[i][j] = aux
    #     else:
    #         pass
    #     return new_board

    # @staticmethod
    # def backtrace(parent, root):
    #     s = Solver()
    #     path = [s.solution.state]
    #     while path[-1] != root.state:
    #         path.append(parent[path[-1]])
    #     path.reverse()
    #     return path

    # def bfs(self):
    #     root = Node()
    #
    #     if root.state == self.solution.state:
    #         print("eita")
    #         return root.board
    #
    #     frontier = deque()  # Creating a FIFO (queue)
    #     frontier.append(root)  # Adding the root to the frontier (which will be following explored)
    #     explored = set()  # Creating an empty set to store the explored notes
    #     explored.add(root.state)
    #     # a = 0
    #     # checking if the queue is empty
    #     while frontier:
    #         node = frontier.popleft()  # Removing the first element of the queue (will be explored)
    #
    #         if node.state == self.solution.state:
    #             return node
    #
    #         # problem being solved
    #         i, j = Solver.find_blank_space(node.board)  # Find the tuple (i, j) with the zero location
    #         movements = Solver.board_movements[(i, j)]
    #         for movement in movements:
    #
    #             # Creating the new board for the child node based on one of the allowed movements
    #             new_board = Solver.change_element_position(node.board, (i, j), movement)
    #             child_node = Node(Solver.empty_board)
    #             child_node.board = new_board
    #
    #             if child_node.state not in explored:
    #                 child_node.parent = node
    #                 frontier.appendleft(child_node)
    #                 explored.add(child_node.state)
    #     return "error"

