from pprint import pprint
import json
import time
import tracemalloc

# Typealias to improve reading
GameState = list[list[int]]

def print_execution_stats(time, currentMemory, peakMemory):
    '''Prints execution time and memory that was used to solve games.'''

    print(f"""
- Elapsed time: {time:.6f} s
- Current memory used: {currentMemory / 10**6:.6f} MB
- Peak memory used: {peakMemory / 10**6:.6f} MB\n""")

def get_row_numbers(state: GameState, row: int) -> set[int]:
    '''Returns all numbers in the row being checked.'''

    return set(state[row])

def get_column_numbers(state: GameState, column: int) -> set[int]:
    '''Returns all numbers in the column being checked.'''

    return {state[row][column] for row in range(9)}

def get_subgrid_numbers(state: GameState, row: int, column: int) -> set[int]:
    '''Returns all numbers in the subgrid being checked.'''

    start_row = (row // 3) * 3
    start_column = (column // 3) * 3
    return {state[start_row + i][start_column + j] for i in range(3) for j in range(3)}

def get_possible_numbers(state: GameState, row: int, column: int) -> list[int]:
    '''Gets all possible numbers considering row, column and subgrid for current number.'''

    # Union of all sets returns used numbers in row, column and subgrid
    used_numbers = get_row_numbers(state, row) | get_column_numbers(state, column) | get_subgrid_numbers(state, row, column)
    return list(set(range(1, 10)) - used_numbers)

def is_row_solved(state: GameState, row: int) -> bool:
    '''Checks if the row contains all numbers from 1 to 9.'''

    # The row being checked must contain all numbers
    return sorted(state[row]) == list(range(1, 10))

def is_column_solved(state: GameState, column: int) -> bool:
    '''Checks if the column contains all numbers from 1 to 9.'''

    return sorted(state[row][column] for row in range(9)) == list(range(1, 10))

def is_subgrid_solved(state: GameState, row: int, column: int) -> bool:
    '''Checks if the subgrid contains all numbers from 1 to 9.'''

    # Calculates the starting coordinate
    start_row = (row // 3) * 3
    start_column = (column // 3) * 3

    # Gets all numbers in current subgrid
    values = [state[start_row + i][start_column + j] for i in range(3) for j in range(3)]
    return sorted(values) == list(range(1, 10))


def is_game_solved(state):
    '''Checks if game is solved, by testing all rows, columns and subgrids in current `GameState`.'''

    for row in range(len(state)):
        if not is_row_solved(state, row):
            return False
        
    for column in range(len(state[0])):
        if not is_column_solved(state, column):
            return False
        
    for row in range(0, len(state), 3):
        for column in range(0, len(state[0]), 3):
            if not is_subgrid_solved(state, row, column):
                return False
            
    return True

def dfs(state: GameState) -> bool:
    '''Executes a Depth-First-Search algorithm in the desired `GameState`.'''

    for row in range(len(state)):
        for column in range(len(state[row])):
            # If the current cell 
            if state[row][column] == 0:
                for num in get_possible_numbers(state, row, column):
                    state[row][column] = num
                    if dfs(state):
                        return True
                    
                    state[row][column] = 0
                return False

    return is_game_solved(state)

# Loads the initial state from JSON
f = open("initial_state.json")
game = json.load(f)

start_time = time.time()
tracemalloc.start()

solved = dfs(game)

current, peak = tracemalloc.get_traced_memory()

tracemalloc.stop()
end_time = time.time()
elapsed_time = end_time - start_time

if solved:
    print("Solution found!")
    pprint(game)
    print_execution_stats(elapsed_time, current, peak)
    
else: print("Solution not found.")

f.close()