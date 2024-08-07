from pprint import pprint
import json

numbers_list = [1,2,3,4,5,6,7,8,9]

def is_line_solved(state: list[list[int]], line: int) -> bool:
    for i in numbers_list:
        # The line being checked must contain all numbers,
        # otherwise it is not solved
        if not state[line].__contains__(i):
            return False

    return True

def is_row_solved(state: list[list[int]], row: int) -> bool:
    stateRow = []
    # Transposes the desired row into an array
    for i in range(len(state)):
        for j in range(len(state[i])):
            if j == row:
                stateRow.append(state[i][j])

    # The row must contain all numbers,
    # otherwise it is not solved
    for i in numbers_list:
        if not stateRow.__contains__(i):
            return False
    
    return True

def is_square_solved(state: list[list[int]], square: int) -> bool:
    mappedSquare = []
    

# Loads the initial state from JSON
f = open("initial_state.json")
initial_state = json.load(f)

pprint(is_row_solved(initial_state, 0))

f.close()