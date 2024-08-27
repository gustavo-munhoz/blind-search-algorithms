import time
import tracemalloc

from dfs_solver import DFSSudokuSolver
from bfs_solver import BFSSudokuSolver
from greedy_solver import GreedySudokuSolver
from a_star_solver import AStarSudokuSolver
from helper_methods import *
from sudoku_benchmark import SudokuBenchmark
from game_factory import GameFactory

# Typealias to improve reading
GameState = list[list[int]]

algorithms = ["DFS", "BFS"]#, "Greedy", "A*"]

print("\nWelcome to sudoku solver!")
print("Which algorithm would you like to test?\n")
print("(1) Depth-First-Algorithm")
print("(2) Breadth-First-Algorithm")
print("(3) Greedy Algorithm")
print("(4) A* Algorithm")
print("(0) Execute benchmark of all")

algorithm = int(input("\nChoose an option: "))

# If benchmark is selected, will execute and exit the program.
if algorithm == 0:
    print("Loading all games...")
    game_factory = GameFactory()
    sudoku_games = []
    for i in range(81):
        sudoku_games.append(game_factory.generate_puzzle(i))

    benchmark = SudokuBenchmark(algorithms, sudoku_games)
    runs = [81]
    benchmark.run_benchmark(runs)
    exit()

# User chooses how many cases, but graphs won't be plotted.

print("Great! How many cases would you like to run? Max: 32610")

games_count = int(input("Choose an option: "))

print("Loading games...")

# Loads games from JSON
sudoku_games = load_random_n_sudoku_games(games_count)

i = 0
elapsed_times = []
current_memories = []
peak_memories = []

for game in sudoku_games:
    i += 1
    print(f"Solving game #{i} with {algorithms[algorithm - 1]}...")
    solver = None

    match algorithm - 1:
        case 0:
            solver = DFSSudokuSolver(game)
        case 1:
            solver = BFSSudokuSolver(game)
        case 2:
            solver = GreedySudokuSolver(game)
        case 3:
            solver = AStarSudokuSolver(game)

    start_time = time.time()
    tracemalloc.start()

    solved = solver.solve()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()
    end_time = time.time()
    elapsed_time = end_time - start_time

    elapsed_times.append(elapsed_time)
    current_memories.append(current)
    peak_memories.append(peak)

elapsed_time_sum = sum(elapsed_times)
current_memory_sum = sum(current_memories)
peak_memory_sum = sum(peak_memories)

print_performance_summary(games_count, elapsed_time_sum, current_memory_sum, peak_memory_sum,
                          elapsed_times, current_memories, peak_memories)