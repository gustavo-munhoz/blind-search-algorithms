from sudoku_solver import SudokuSolver, GameState
from collections import deque
import copy

class BFSSudokuSolver(SudokuSolver):
    def solve(self) -> GameState:
        '''Executes a Breadth-First-Search algorithm in the desired `GameState`.'''
        
        # Using a deque allows quick manipulation of states being stored.
        queue = deque([self.state])

        while queue:
            # Gets the oldest state added to the deque, as the "top-level" states should always be searched first.
            current_state = queue.popleft()

            for row in range(len(current_state)):
                for column in range(len(current_state[row])):
                    if current_state[row][column] == 0:
                        # If the current number is unassigned, will save a state copy for each possible value.
                        for num in self.get_possible_numbers(row, column, current_state):
                            new_state = copy.deepcopy(current_state)
                            new_state[row][column] = num
                            queue.append(new_state)
                        break
                else:
                    # Do nothing if the cell is already assigned.
                    continue
                break
            else:
                # Check if the game is solved when there aren't any cells left.
                if self.is_game_solved(current_state):
                    return current_state

        return None  # Return None if no solution is found
    
    
