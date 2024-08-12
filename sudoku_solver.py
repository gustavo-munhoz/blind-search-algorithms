from abc import ABC, abstractmethod

# Typealias to improve reading
GameState = list[list[int]]

class SudokuSolver(ABC):
    def __init__(self, initial_state: GameState):
        self.state = initial_state

    def print_execution_stats(self, time, currentMemory, peakMemory):
        '''Prints execution time and memory that was used to solve games.'''
        print(f"""
- Elapsed time: {time:.6f} s
- Current memory used: {currentMemory / 10**6:.6f} MB
- Peak memory used: {peakMemory / 10**6:.6f} MB\n""")
    
    def print_sudoku_board(self):
        '''Prints the game board in a more comprehensible way.'''
        for row in range(len(self.state)):
            if row % 3 == 0 and row != 0:
                print("-" * 21)

            for col in range(len(self.state[row])):
                if col % 3 == 0 and col != 0:
                    print("| ", end="")

                if col == 8:
                    print(self.state[row][col])
                else:
                    print(str(self.state[row][col]) + " ", end="")

    def get_row_numbers(self, row: int) -> set[int]:
        '''Returns all numbers in the row being checked.'''
        return set(self.state[row])

    def get_column_numbers(self, column: int) -> set[int]:
        '''Returns all numbers in the column being checked.'''
        return {self.state[row][column] for row in range(9)}

    def get_subgrid_numbers(self, row: int, column: int) -> set[int]:
        '''Returns all numbers in the subgrid being checked.'''
        start_row = (row // 3) * 3
        start_column = (column // 3) * 3
        return {self.state[start_row + i][start_column + j] for i in range(3) for j in range(3)}

    def get_possible_numbers(self, row: int, column: int) -> list[int]:
        '''Gets all possible numbers considering row, column and subgrid for current number.'''

        # Union of all sets returns used numbers in row, column and subgrid
        used_numbers = self.get_row_numbers(row) | self.get_column_numbers(column) | self.get_subgrid_numbers(row, column)
        return list(set(range(1, 10)) - used_numbers)

    def is_row_solved(self, state: GameState, row: int) -> bool:
        '''Checks if the row contains all numbers from 1 to 9.'''

        # The row being checked must contain all numbers
        return sorted(state[row]) == list(range(1, 10))

    def is_column_solved(self, state: GameState, column: int) -> bool:
        '''Checks if the column contains all numbers from 1 to 9.'''

        return sorted(state[row][column] for row in range(9)) == list(range(1, 10))

    def is_subgrid_solved(self, state: GameState, row: int, column: int) -> bool:
        '''Checks if the subgrid contains all numbers from 1 to 9.'''

        # Calculates the starting coordinate
        start_row = (row // 3) * 3
        start_column = (column // 3) * 3

        # Gets all numbers in current subgrid
        values = [state[start_row + i][start_column + j] for i in range(3) for j in range(3)]
        return sorted(values) == list(range(1, 10))


    def is_game_solved(self, state: GameState) -> bool:
        '''Checks if game is solved, by testing all rows, columns and subgrids in the provided `GameState`.'''

        for row in range(len(state)):
            if not self.is_row_solved(state, row):
                return False
        
        for column in range(len(state[0])):
            if not self.is_column_solved(state, column):
                return False
        
        for row in range(0, len(state), 3):
            for column in range(0, len(state[0]), 3):
                if not self.is_subgrid_solved(state, row, column):
                    return False
            
        return True


    @abstractmethod
    def solve(self) -> GameState:
        '''Solve the Sudoku puzzle using a specific algorithm (DFS, BFS, etc.).'''
        pass