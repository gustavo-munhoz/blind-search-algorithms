from pprint import pprint
import json

# Typealias to improve reading
GameState = list[list[int]]

def get_possible_numbers(from_list: list[int]) -> list[int]:
    return filter(not list(range(1, 10).__contains__()))

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

def dfs(state: GameState):
    for row in range(len(state)):
        for column in range(len(state[row])):
            if state[row][column] == 0:
                print(f"Unassigned cell at ({row}, {column})")
            else:
                if is_row_solved(state, row) and \
                   is_column_solved(state, column) and \
                   is_subgrid_solved(state, row, column):
                    return True
                else:
                    return False

    
    return True


# Loads the initial state from JSON
f = open("initial_state.json")
initial_state = json.load(f)

dfs(state=initial_state)

f.close()