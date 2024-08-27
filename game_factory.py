import random

class GameFactory:
    '''This class creates random games that can be used for testing.'''
    def __init__(self):
        pass

    def generate_full_board(self):
        board = [[0 for _ in range(9)] for _ in range(9)]
        self._fill_board(board)
        return board

    def _fill_board(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if self._is_valid(board, i, j, num):
                            board[i][j] = num
                            if self._fill_board(board):
                                return True
                            board[i][j] = 0
                    return False
        return True

    def _is_valid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def create_puzzle(self, full_board, num_holes=40):
        puzzle = [row[:] for row in full_board]
        holes = 0
        while holes < num_holes:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if puzzle[row][col] != 0:
                puzzle[row][col] = 0
                holes += 1
        return puzzle

    def generate_puzzle(self, num_holes=40):
        full_board = self.generate_full_board()
        puzzle = self.create_puzzle(full_board, num_holes)
        return puzzle