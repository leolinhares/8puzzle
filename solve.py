from puzzle_solver import Solver
import time
from tkinter import *
import itertools


def main():
    # Solver.draw_path(Solver.breadth_first_search())
    window = Tk()
    window.title("8 Puzzle Solver")
    window.geometry("350x450")

    label = Label(window, text='8Puzzle Random Example\n')
    label.pack()

    start_time = time.time()
    solution_node, number_of_nodes = Solver.breadth_first_search()

    nodes = Label(text="Nodes BFS: %d" % number_of_nodes)
    nodes.pack()

    path, move_list, number_of_moves = Solver.draw_path(solution_node)

    moves = Label(text="Moves BFS: %d" % number_of_moves)
    moves.pack()

    elapsed_time = Label(text="Time BFS: %f seconds\n" % (time.time() - start_time))
    elapsed_time.pack()





    start_time2 = time.time()
    solution_node2, number_of_nodes2 = Solver.a_star()

    nodes2 = Label(text="Nodes A*m: %d" % number_of_nodes2)
    nodes2.pack()

    path2, move_list2, number_of_moves2 = Solver.draw_path(solution_node)

    moves2 = Label(text="Moves A*m: %d" % number_of_moves2)
    moves2.pack()

    elapsed_time2 = Label(text="Time A*m: %f seconds\n" % (time.time() - start_time2))
    elapsed_time2.pack()


    start_time3 = time.time()
    solution_node3, number_of_nodes3 = Solver.a_star(1)

    nodes3 = Label(text="Nodes A*h: %d" % number_of_nodes3)
    nodes3.pack()

    path3, move_list3, number_of_moves3 = Solver.draw_path(solution_node)

    moves3 = Label(text="Moves A*h: %d" % number_of_moves3)
    moves3.pack()

    elapsed_time3 = Label(text="Time A*h: %f seconds\n" % (time.time() - start_time3))
    elapsed_time3.pack()

    it = itertools.cycle(path)
    it_moves = itertools.cycle(move_list)

    lbl = Label(text="Press next")
    lbl.pack()
    lbl_move = Label(text="")
    lbl_move.pack()

    def generate_next():
        lbl.configure(text=next(it))
        lbl_move.configure(text=next(it_moves))

    btn_solver = Button(window, text="Next Step", command=generate_next)
    btn_solver.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
