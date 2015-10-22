from puzzle_solver import Solver
import time
start_time = time.time()
print(Solver.breadth_first_search())
print("--- %s seconds ---" % (time.time() - start_time))

