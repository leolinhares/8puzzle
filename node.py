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
            puzzle = eight_puzzle.generate_random_puzzle()
            self._board = [elem[:] for elem in puzzle]
            # self._board = [[6, 4, 0], [8, 1, 7], [5, 2, 3]]
            # self._board = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
            # self._board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
            # self._board = [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
            # self._board = [[8, 0, 6], [5, 4, 7], [2, 3, 1]]
            # self._board = [[0, 8, 4], [2, 6, 1], [3, 5, 7]]
            # self._board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
            # self._board = [[7, 8, 1], [2, 3, 5], [0, 6, 4]]

            # 22 moves, 23 nodes, 3seconds
            # self._board = [[6, 5, 4], [7, 3, 1], [0, 8, 2]]

            # 24 moves, 25 nodes, 5.94 seconds
            # self._board = [[7, 4, 8], [1, 5, 3], [0, 6, 2]]

            # A star 7163 nodes, 0.46s
            # BFS 0.23s 5101 node, 16 moves
            # self._board = [[0, 4, 1], [7, 3, 6], [5, 8, 2]]

            # self._board = [[3, 4, 6], [2, 1, 5], [0, 7, 8]]
            # self._board = [[3, 1, 8], [2, 5, 6], [7, 4, 0]]

            # self._board = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]
            # self._board = [[2, 7, 3], [4, 8, 1], [0, 6, 5]]
            # self._board = [[3, 2, 7], [5, 6, 8], [4, 1, 0]]

            # self._board = [[1,2,3], [4,5,6], [7,8,0]]

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
