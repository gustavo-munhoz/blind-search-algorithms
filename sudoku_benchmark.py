import time
import tracemalloc
import matplotlib.pyplot as plt

from dfs_solver import DFSSudokuSolver
from bfs_solver import BFSSudokuSolver
from greedy_solver import GreedySudokuSolver
from a_star_solver import AStarSudokuSolver

GameState = list[list[int]]

class SudokuBenchmark:
    '''This class runs the desired algorithms and plots the graphs with the measured results.'''
    
    def __init__(self, algorithms: list[str], sudoku_games: list[GameState]):
        self.algorithms = algorithms
        self.sudoku_games = sudoku_games
        self.results = {algorithm: {"elapsed_times": [], "current_memories": [], "peak_memories": []}
                        for algorithm in algorithms}

    def run_benchmark(self, runs: list[int]):
        for algorithm_index, algorithm_name in enumerate(self.algorithms):
            for run_count in runs:
                print(f"Running {algorithm_name} with {run_count} games...")
                for i in range(run_count):
                    print(f"Solving game #{i + 1} with {algorithm_name}...")
                    solver = self.get_solver(algorithm_index, self.sudoku_games[i])

                    start_time = time.time()
                    tracemalloc.start()

                    solver.solve()

                    _, peak = tracemalloc.get_traced_memory()
                    tracemalloc.stop()
                    end_time = time.time()

                    elapsed_time = (end_time - start_time) * 1000

                    self.results[algorithm_name]["elapsed_times"].append(elapsed_time)
                    self.results[algorithm_name]["peak_memories"].append(peak)

        self.plot_results()

    def get_solver(self, algorithm_index: int, game: GameState):
        match algorithm_index:
            case 0:
                return DFSSudokuSolver(game)
            case 1:
                return BFSSudokuSolver(game)
            case 2:
                return GreedySudokuSolver(game)
            case 3:
                return AStarSudokuSolver(game)

    def plot_results(self):
        fig, axs = plt.subplots(2, 1, figsize=(10, 10))

        for algorithm_name, metrics in self.results.items():
            runs = range(1, len(metrics["elapsed_times"]) + 1)
            axs[0].plot(runs, metrics["elapsed_times"], label=algorithm_name)
            axs[1].plot(runs, metrics["peak_memories"], label=algorithm_name)

        axs[0].set_title('Elapsed Time Comparison')
        axs[0].set_xlabel('Unassigned cells')
        axs[0].set_ylabel('Time [log(ms)]')
        axs[0].set_yscale('log')

        axs[1].set_title('Peak Memory Usage Comparison')
        axs[1].set_xlabel('Unassigned cells')
        axs[1].set_ylabel('Memory [log(bytes)]')
        axs[1].set_yscale('log')

        for ax in axs:
            ax.legend()
            ax.grid(True)

        plt.tight_layout()
        plt.show()