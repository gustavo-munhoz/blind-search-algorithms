from sudoku_solver import SudokuSolver, GameState

class DFSSudokuSolver(SudokuSolver):
    def solve(self) -> GameState:
        '''Executes a Depth-First-Search algorithm in the desired `GameState`.'''

        # Encapsulate dfs logic inside `solve()` method.
        def dfs(state: GameState) -> bool:
            for row in range(len(state)):
                for column in range(len(state[row])):
                    # If the cell is unassigned, will execute DFS recursively until success or backtrack.
                    if state[row][column] == 0:
                        for num in self.get_possible_numbers(row, column):
                            state[row][column] = num
                            if dfs(state):
                                return True
                        
                            # Reset cell for backtracking
                            state[row][column] = 0
                        return False

            return self.is_game_solved()

        if dfs(self.state):
            return self.state
        else:
            return None