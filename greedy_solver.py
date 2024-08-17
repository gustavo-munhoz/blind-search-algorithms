from sudoku_solver import SudokuSolver, GameState

class GreedySudokuSolver(SudokuSolver):
    def solve(self) -> GameState:
        '''Executes a Greedy algorithm in the desired `GameState`, based on cells that have the least plays possible.'''

        def backtrack() -> bool:
            min_options = 10
            best_cell = None
            best_options = None

            for row in range(len(self.state)):
                for column in range(len(self.state[row])):
                    if self.state[row][column] == 0:
                        options = self.get_possible_numbers(row, column)

                        # Found a cell that has less options than others
                        if len(options) < min_options:
                            min_options = len(options)
                            best_cell = (row, column)
                            best_options = options
                        
            if best_cell is None:
                # All cells are assigned to a number
                return self.is_game_solved()
            
            row, column = best_cell
            for option in best_options:
                # Iterate over options to find a valid one.
                self.state[row][column] = option
                if backtrack():
                    return True

                # Will reset the cell if backtrack is triggered
                self.state[row][column] = 0
            
            return False
    
        return self.state if backtrack() else None