from node import Node
from collections import deque
import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def exists(self, item):
        return item in (x[1] for x in self.elements)


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
            child.move = movement
            child.parent = parent
            children.append(child)
        return children

    @staticmethod
    def number_of_misplaced_tiles(board):
        misplaced_tiles = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != Solver.solution.board[i][j]:
                    misplaced_tiles += 1
        return misplaced_tiles


    @staticmethod
    def calculate_distance(board):
        manhattan_distance = 0
        for i in range(3):
            for j in range(3):
                value = board[i][j]
                if value != 0:
                    targetx = (value - 1) // 3
                    targety = (value - 1) % 3
                    dx = i - targetx
                    dy = j - targety
                    manhattan_distance = manhattan_distance + abs(dx) + abs(dy)
        return manhattan_distance

    @staticmethod
    def breadth_first_search():
        root = Node()
        visited, queue = set(), deque([root])
        while queue:
            node = queue.pop()
            if node.state in visited:
                continue

            # if node.state == Solver.solution.state:
            #     return node

            visited.add(node.state)

            for child in Solver.generate_children(node):
                if child.state not in visited:
                    if child.state == Solver.solution.state:
                        print("Number of visited nodes: %d" % len(visited))
                        return child
                    else:
                        queue.appendleft(child)
        return "Error"

    @staticmethod
    def draw_path(node_result):

        path = []
        aux = node_result
        while aux.parent is not None:
            path.append((aux, aux.move))
            aux = aux.parent

        path.append((aux, aux.move))

        print(len(path))

        path.reverse()
        for node, move in path:
            print(move)
            print(Solver.calculate_distance(node.board))
            print(node)


    @staticmethod
    def hamming(board):
        misplaced_tiles = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != Solver.solution.board[i][j]:
                    misplaced_tiles += 1
        return misplaced_tiles

    @staticmethod
    def distance_to_objective(board):
        pass

    @staticmethod
    def to_matrix(string):
        l = list(map(int, string))
        matrix = []
        while l:
            matrix.append(l[:3])
            l = l[3:]
        return matrix

    @staticmethod
    def a_star():
        visited, frontier = set(), PriorityQueue()

        root = Node()
        priority = Solver.calculate_distance(root.board)
        frontier.put(root.state, root.calculate_path_cost() + priority)

        while frontier:
            # removing the frontier lowest priority node (PriorityQueue)
            node_state = frontier.get()
            matrix = Solver.to_matrix(node_state)
            node = Node(matrix)

            # if the node is the solution, return the node
            if node_state == Solver.solution.state:
                print("number of node: %d" % len(visited))
                return node_state

            # adding node to visited set
            visited.add(node_state)

            # exploring the node children
            for child in Solver.generate_children(node):
                priority = Solver.calculate_distance(child.board)
                path_cost = child.calculate_path_cost()
                if child.state not in visited:
                    frontier.put(child.state, priority+path_cost)
                # elif frontier.exists(child.state):
                    #     if child priority > total:
                    #         exchange
        return "Error"
