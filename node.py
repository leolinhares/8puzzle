from copy import deepcopy


class Node:
    def __init__(self, board=None):
        if board:
            self._board = deepcopy(board)
        else:
            # self._board = [[6, 4, 0], [8, 1, 7], [5, 2, 3]]
            # self._board = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
            # self._board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
            # self._board = [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
            # self._board = [[8, 0, 6], [5, 4, 7], [2, 3, 1]]
            self._board = [[0, 8, 4], [2, 6, 1], [3, 5, 7]]
            # self._board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
            # self._board = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]

            # self._board = [[1,2,3], [4,5,6], [7,8,0]]
        self._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def state(self):
        """
        This property(it is a object node variable with just a getter)
        will identify a node by a unique string
        :return: hash of the node
        """

        '''
        for innerlist in outerlist:
            for item in innerlist:
        '''
        node_str = ''.join(str(item) for row in self.board for item in row)
        return node_str
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
