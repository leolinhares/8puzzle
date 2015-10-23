from puzzle_solver import Solver
import time
start_time = time.time()

Solver.draw_path(Solver.breadth_first_search())
print(Solver.a_star())
print("--- %s seconds ---" % (time.time() - start_time))
