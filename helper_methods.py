import math
import json
import random

def print_performance_summary(cases, elapsed_time_sum, current_memory_sum, peak_memory_sum,
                              elapsed_times, current_memories, peak_memories):

    avg_time = elapsed_time_sum / cases
    avg_current_memory = current_memory_sum / cases
    avg_peak_memory = peak_memory_sum / cases

    time_variance = sum((x - avg_time) ** 2 for x in elapsed_times) / cases
    time_std_dev = math.sqrt(time_variance)

    current_memory_variance = sum((x - avg_current_memory) ** 2 for x in current_memories) / cases
    current_memory_std_dev = math.sqrt(current_memory_variance)

    peak_memory_variance = sum((x - avg_peak_memory) ** 2 for x in peak_memories) / cases
    peak_memory_std_dev = math.sqrt(peak_memory_variance)

    print("\nPerformance Summary\n" + "-" * 30)
    print(f"Average time: {avg_time:.4f} seconds")
    print(f"Time standard deviation: {time_std_dev:.4f} seconds")
    print(f"Average current memory: {avg_current_memory:.3f} MB")
    print(f"Current memory standard deviation: {current_memory_std_dev:.3f} MB")
    print(f"Average peak memory: {avg_peak_memory:.3f} MB")
    print(f"Peak memory standard deviation: {peak_memory_std_dev:.3f} MB\n")

def load_random_n_sudoku_games(n):
    with open("sudoku_games.json", 'r') as file:
        sudoku_games = json.load(file)
    
    random.seed(2)
    random_games = random.sample(sudoku_games, n)
    
    return random_games