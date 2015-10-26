from puzzle_solver import Solver
import time


# def main():
#     option = True
#     while option:
#         print("""
#             1. Solve a randomly generated puzzle using BFS
#             2. Solve a randomly generated puzzle using A* (hamming heuristic)
#             3. Solve a randomly generated puzzle using A* (manhattan heuristic)
#
#             Press enter to quit
#             """)
#         option = input("\nWhat do you like to do? ")
#         if option == "1":
#             start_time = time.time()
#             Solver.draw_path(Solver.breadth_first_search())
#             print("--- %s seconds ---" % (time.time() - start_time))
#
#         elif option == "2":
#             start_time = time.time()
#             node_state, all_paths = Solver.a_star()
#             print(node_state)
#             print(len(all_paths))
#             print("--- %s seconds ---" % (time.time() - start_time))
#         elif option == "3":
#             pass
#         elif option != "":
#             print("\nInvalid choice")


def main():
    start_time = time.time()
    Solver.draw_path(Solver.breadth_first_search())
    # node_state, all_paths = Solver.a_star()

    # lista = []
    #
    # def find_parent(son):
    #     for parent, child in all_paths.iteritems():
    #         if child == son:
    #             lista.append(parent)
    #             find_parent(parent)

    # print(node_state)
    # print(len(all_paths))
    # find_parent(node_state)
    # print(lista)

    # Solver.draw_path(all_paths[-1])
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
