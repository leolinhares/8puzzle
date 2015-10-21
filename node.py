from copy import deepcopy


class Node:
    def __init__(self, board=None):
        if board:
            self.__board = deepcopy(board)
        else:
            self.__board = [[7, 5, 6], [4, 3, 2], [0, 1, 8]]
        # self.child = set()  # unsorted collection of with no duplicate elements

    @property
    def state(self):
        """
        :return: hash of the node
        """
        return str(self)

    def get_board(self):
        return self.__board

    def set_board(self, new_board):
        self.__board = deepcopy(new_board)

    def __str__(self):
        str1 = ''
        for row in self.__board:
            str1 = str1 + "\n" + ''.join(str(e) for e in row)
        return str1

    def __eq__(self, other):
        return self.state == other.state






