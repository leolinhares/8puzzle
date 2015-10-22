from puzzle_solver import Solver
import time
start_time = time.time()
s = Solver()
print(s.bfs())
print("--- %s seconds ---" % (time.time() - start_time))

