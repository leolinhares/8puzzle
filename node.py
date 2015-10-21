from copy import deepcopy


class Node:
    def __init__(self, board=None):
        if board:
            self._board = deepcopy(board)
        else:
            self._board = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
            # self.child = set()  # unsorted collection of with no duplicate elements

    @property
    def state(self):
        """
        This property(it is a object node variable with just a getter)
        will identify a node by a unique string
        :return: hash of the node
        """
        return str(self)

    '''
        This property creates the getter for the board object and
        it is possible to access it by just: object.board instead of
        using object.get_board
    '''
    @property
    def board(self):
        return self._board

    '''
        The property way of defining a setter
        Instead of typing object.set_board(value), one can just
        use it like a normal variable: object.board = value
    '''
    @board.setter
    def board(self, new_board):
        self._board = deepcopy(new_board)

    def __str__(self):
        """
        Method designed to overwrite the print function of a node.
        :return: a properly formatted node printed
        """
        str1 = ''
        for row in self.board:
            str1 = str1 + "\n" + ''.join(str(e) for e in row)
        return str1

    def __eq__(self, other):
        """
        Overwritten method which compares if two nodes are equal
        :param other: the other node object to be compared
        :return: if they are equal or not
        """
        return self.state == other.state
