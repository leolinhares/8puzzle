def find_blank_space(board):
    """
    :param board: matrix[3][3]
    :return: a tuple with the position of the element zero.
    """
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == 0:
                return i, j


board_movements = {(0, 0): ('R', 'D'),
                   (0, 1): ('L', 'R', 'D'),
                   (0, 2): ('L', 'D'),
                   (1, 0): ('R', 'U', 'D'),
                   (1, 1): ('L', 'R', 'U', 'D'),
                   (1, 2): ('U', 'L', 'D'),
                   (2, 0): ('U', 'R'),
                   (2, 1): ('R', 'U', 'L'),
                   (2, 2): ('U', 'L')}


def change_element_position(board, zero_position, movement):
    """
    :param board: matrix[3][3]
    :param position: tuple with the position of element zero
    :param movement: with move will be executed
    :return: a new board after the change of an element's position
    """
    new_board = board
    i, j = zero_position
    if movement == 'L':
        aux = new_board[i][j-1]
        new_board[i][j-1] = 0
        new_board[i][j] = aux
    elif movement == 'U':
        aux = new_board[i-1][j]
        new_board[i-1][j] = 0
        new_board[i][j] = aux
    elif movement == 'R':
        aux = new_board[i][j+1]
        new_board[i][j+1] = 0
        new_board[i][j] = aux
    elif movement == 'D':
        aux = new_board[i+1][j]
        new_board[i+1][j] = 0
        new_board[i][j] = aux
    else:
        pass
    return new_board


board = [[1, 2, 3], [5, 4, 9], [0, 6, 7]]

print(find_blank_space(board))
