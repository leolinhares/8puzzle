import eight_puzzle


class Node:
    def __init__(self, board=None):
        self.move = ''
        self.path_cost = 0
        self.priority = 0
        self.parent = None

        if board:
            self._board = [elem[:] for elem in board]
        else:
            # puzzle = eight_puzzle.generate_random_puzzle()
            # self._board = [elem[:] for elem in puzzle]
            self._board = [[1, 0, 6], [3, 2, 5], [7, 8, 4]]

    def calculate_path_cost(self):
        if self.parent is not None:
            self.path_cost = self.parent.path_cost + 1
        return self.path_cost

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

    @property
    def board(self):
        """
        This property creates the getter for the board object and
        it is possible to access it by just: object.board instead of
        using object.get_board
        """
        return self._board

    @board.setter
    def board(self, new_board):
        """
        The property way of defining a setter
        Instead of typing object.set_board(value), one can just
        use it like a normal variable: object.board = value
        """
        self._board = [elem[:] for elem in new_board]

    def __str__(self):
        """
        Method designed to overwrite the print function of a node.
        :return: a properly formatted node printed
        """
        str1 = ''
        for row in self.board:
            str1 = str1 + ' '.join(str(e) for e in row) + '\n'
        return str1

    def __eq__(self, other):
        """
        Overwritten method which compares if two nodes are equal
        :param other: the other node object to be compared
        :return: if they are equal or not
        """
        return self.state == other.state
