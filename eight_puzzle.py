from random import *


def generate_random_puzzle():
    """
    :return: a randomly generated 8puzzle matrix
    """
    # generating a (0-9) list
    puzzle_list = [item for item in range(9)]

    # shuffling the list
    shuffle(puzzle_list)

    if is_solvable(puzzle_list):
        # transforming the list into a matrix[3][3]
        puzzle_matrix = []
        while puzzle_list:
            puzzle_matrix.append(puzzle_list[:3])
            puzzle_list = puzzle_list[3:]
        return puzzle_matrix
    else:
        return generate_random_puzzle()


def is_solvable(puzzle_list):
    # the puzzle is solvable if the number of inversions is even
    if count_inversions(puzzle_list) % 2 == 0:
        return True
    return False


def count_inversions(puzzle_list):
    inversions = 0
    for i in range(8):
        for j in range(i+1, 9):
            if puzzle_list[j] and puzzle_list[i] and puzzle_list[i] > puzzle_list[j]:
                inversions += 1
    return inversions
