import json
import time
import tracemalloc
from dfs_solver import DFSSudokuSolver
from bfs_solver import BFSSudokuSolver

# Typealias to improve reading
GameState = list[list[int]]

# Loads the initial state from JSON
f = open("game2.json")
game = json.load(f)
solver = DFSSudokuSolver(game)

start_time = time.time()
tracemalloc.start()

solved = solver.solve()

current, peak = tracemalloc.get_traced_memory()

tracemalloc.stop()
end_time = time.time()
elapsed_time = end_time - start_time

if solved is not None:
    print("Solution found!\n")
    solver.print_sudoku_board()
    solver.print_execution_stats(elapsed_time, current, peak)
    
else: print("Solution not found.")

f.close()