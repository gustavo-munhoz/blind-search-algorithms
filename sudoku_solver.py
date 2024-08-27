from abc import ABC, abstractmethod

# Typealias to improve reading
GameState = list[list[int]]

class SudokuSolver(ABC):
    '''An abstract class that contains useful methods for implementing different sudoku solving algorithms.'''
    
    def __init__(self, initial_state: GameState):
        self.state = initial_state

    def print_execution_stats(self, time, currentMemory, peakMemory):
        '''Prints execution time and memory that was used to solve games.'''
        print(f"""
- Elapsed time: {time:.6f} s
- Current memory used: {currentMemory / 10**6:.6f} MB
- Peak memory used: {peakMemory / 10**6:.6f} MB\n""")
    
    def print_sudoku_board(self, state: GameState = None):
        '''Prints the game board in a more comprehensible way.'''
        if state is None:
            state = self.state
        for row in range(len(state)):
            if row % 3 == 0 and row != 0:
                print("-" * 21)
            for col in range(len(state[row])):
                if col % 3 == 0 and col != 0:
                    print("| ", end="")
                if col == 8:
                    print(state[row][col])
                else:
                    print(str(state[row][col]) + " ", end="")

    def get_row_numbers(self, row: int, state: GameState = None) -> set[int]:
        '''Returns all numbers in the row being checked.'''
        if state is None:
            state = self.state
        return set(state[row])

    def get_column_numbers(self, column: int, state: GameState = None) -> set[int]:
        '''Returns all numbers in the column being checked.'''
        if state is None:
            state = self.state
        return {state[row][column] for row in range(9)}

    def get_subgrid_numbers(self, row: int, column: int, state: GameState = None) -> set[int]:
        '''Returns all numbers in the subgrid being checked.'''
        if state is None:
            state = self.state
        start_row = (row // 3) * 3
        start_column = (column // 3) * 3
        return {state[start_row + i][start_column + j] for i in range(3) for j in range(3)}

    def get_possible_numbers(self, row: int, column: int, state: GameState = None) -> list[int]:
        '''Gets all possible numbers considering row, column and subgrid for current number.'''
        if state is None:
            state = self.state
        used_numbers = (self.get_row_numbers(row, state) |
                        self.get_column_numbers(column, state) |
                        self.get_subgrid_numbers(row, column, state))
        return list(set(range(1, 10)) - used_numbers)

    def is_row_solved(self, row: int, state: GameState = None) -> bool:
        '''Checks if the row contains all numbers from 1 to 9.'''
        if state is None:
            state = self.state
        return sorted(state[row]) == list(range(1, 10))

    def is_column_solved(self, column: int, state: GameState = None) -> bool:
        '''Checks if the column contains all numbers from 1 to 9.'''
        if state is None:
            state = self.state
        return sorted(state[row][column] for row in range(9)) == list(range(1, 10))

    def is_subgrid_solved(self, row: int, column: int, state: GameState = None) -> bool:
        '''Checks if the subgrid contains all numbers from 1 to 9.'''
        if state is None:
            state = self.state
        start_row = (row // 3) * 3
        start_column = (column // 3) * 3
        values = [state[start_row + i][start_column + j] for i in range(3) for j in range(3)]
        return sorted(values) == list(range(1, 10))

    def is_game_solved(self, state: GameState = None) -> bool:
        '''Checks if game is solved, by testing all rows, columns and subgrids in current `GameState`.'''
        if state is None:
            state = self.state
        for row in range(len(state)):
            if not self.is_row_solved(row, state):
                return False
        for column in range(len(state[0])):
            if not self.is_column_solved(column, state):
                return False
        for row in range(0, len(state), 3):
            for column in range(0, len(state[0]), 3):
                if not self.is_subgrid_solved(row, column, state):
                    return False
        return True

    @abstractmethod
    def solve(self) -> GameState:
        '''Solve the Sudoku puzzle using a specific algorithm (DFS, BFS, etc.).'''
        pass
