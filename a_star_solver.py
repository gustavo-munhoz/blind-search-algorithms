from sudoku_solver import SudokuSolver, GameState

class AStarSudokuSolver(SudokuSolver):
    def solve(self) -> GameState:
        '''Executes the A* algorithm to solve Sudoku.'''

        # This relates every state with the equivalent estimated cost,
        # which is used to choose the optimal next state.
        weighted_states: dict[int, GameState] = {}

        def heuristic() -> int:
            # Amount of zeros still in the game
            return sum(row.count(0) for row in self.state)

        def f(n) -> int:
            ''' Calculates the estimated cost by adding the heuristic `h` with the cost `g`.'''
            h = heuristic()
            g = n
            return g + h        

        while not self.is_game_solved():
            # `attempts` represents the amount of times cells have been assigned a value
            attempts = 0
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
            
            row, column = best_cell
            for option in best_options:
                attempts += 1
                self.state[row][column] = option
                weighted_states[f(attempts)] = self.state

                if self.solve() is not None:
                    # Finds and returns the state with minimal estimated cost `f`.
                    min_key = min(weighted_states)
                    return weighted_states[min_key]

                # Resets cell
                self.state[row][column] = 0
        
            return None
        
        return self.state

