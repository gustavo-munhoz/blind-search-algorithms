import json
import time
import tracemalloc
from dfs_solver import DFSSudokuSolver
from bfs_solver import BFSSudokuSolver

def load_first_n_sudoku_games(json_path, n):
    with open(json_path, 'r') as file:
        sudoku_games = json.load(file)
    
    first_n_games = sudoku_games[:n]
    
    return first_n_games

def print_performance_summary(cases, elapsed_time_sum, current_memory_sum, peak_memory_sum):
    # Calcula as médias
    avg_time = elapsed_time_sum / cases
    avg_current_memory = current_memory_sum / cases
    avg_peak_memory = peak_memory_sum / cases
    
    # Cabeçalho para a saída
    print("\nPerformance Summary\n" + "-" * 30)
    
    # Formatação com duas casas decimais para tempo e memória
    print(f"Average time: {avg_time:.2f} seconds")
    print(f"Average current memory: {avg_current_memory:.2f} MB")
    print(f"Average peak memory: {avg_peak_memory:.2f} MB\n")

# Typealias to improve reading
GameState = list[list[int]]

algorithms = ["DFS", "BFS"]

print("\nWelcome to sudoku solver!")
print("Which algorithm would you like to test?\n")
print("(1) Depth-First-Algorithm")
print("(2) Breadth-First-Algorithm")
print("(3) All")

algorithm = int(input("\nChoose an option: "))

print("Great! How many cases would you like to run? Max.: 1.000.000")

cases = int(input("Choose an option: "))

print("Loading games...")

# Loads games from JSON
first_n_sudoku_games = load_first_n_sudoku_games("sudoku_games.json", cases)

i = 0
elapsed_time_sum = 0
current_memory_sum = 0
peak_memory_sum = 0

for game in first_n_sudoku_games:
    i += 1
    print(f"Solving game #{i} with {algorithms[algorithm - 1]}...")
    solver = BFSSudokuSolver(game) if algorithm == 1 else DFSSudokuSolver(game) 

    start_time = time.time()
    tracemalloc.start()

    solved = solver.solve()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()
    end_time = time.time()
    elapsed_time = end_time - start_time

    elapsed_time_sum += elapsed_time
    current_memory_sum += current
    peak_memory_sum += peak

print_performance_summary(cases, elapsed_time_sum, current_memory_sum, peak_memory_sum)