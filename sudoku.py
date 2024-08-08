from pprint import pprint
import json
import copy

# Typealias to improve reading
GameState = list[list[int]]

def get_possible_numbers_from(numbers: set[int]) -> list[int]:
    return list(set(range(1, 10)).difference(numbers))

def is_row_solved(state: GameState, row: int) -> bool:
    # The row being checked must contain all numbers
    return sorted(state[row]) == list(range(1, 10))

def is_column_solved(state: GameState, column: int) -> bool:
    column_values = []
    # Transposes the desired column into an array
    for i in range(len(state)):
        for j in range(len(state[i])):
            if j == column:
                column_values.append(state[i][j])    
    
    return sorted(column_values) == list(range(1, 10))

def is_subgrid_solved(state: GameState, row: int, column: int) -> bool:
    # Calculate the starting coordinate
    start_row = (row // 3) * 3
    start_column = (column // 3) * 3

    values = []

    for i in range(3):
        for j in range(3):
            # Stores all numbers inside the subgrid
            values.append(state[start_row + i][start_column + j])

    return sorted(values) == list(range(1, 10))

def dfs(state: GameState) -> bool:
    stateCopy = copy.deepcopy(state)
    
    for row in range(len(state)):
        for column in range(len(state[row])):
            if stateCopy[row][column] == 0:
                for num in get_possible_numbers_from(stateCopy[row]):
                    stateCopy[row][column] = num
                    dfs(stateCopy)
            
    
    return True


# Loads the initial state from JSON
f = open("initial_state.json")
initial_state = json.load(f)

print(dfs(state=initial_state))

f.close()