from puzzle_solver import Solver
import time
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
