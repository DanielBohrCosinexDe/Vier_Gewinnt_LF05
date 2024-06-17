class Board_grid():
    def __init__(self, rows=6, columns=7) -> None:
        self.rows = rows
        self.columns = columns
        self.grid = [[None for _ in range(columns)] for _ in range(rows)]
        
    def initialize_board(self):
        # array = [None for - in rang(6)]
        self.grid = [[None for _ in range(self.columns)] for _ in range(self.rows)]
    
    def drop_piece(self, column, piece):
        for row in reversed(range(self.rows)):
            if self.grid[row][column] is None:
                self.grid[row][column] = piece
                return row
        return None
    
    def is_full(self):
        return all(self.grid[0][col] is not None for col in range(self.columns))
    
    def check_winner(self, piece):
        def check_direction(row, col, dr, dc):
            count = 0
            for _ in range(4):
                if 0 <= row < self.rows and 0 <= col < self.columns and self.grid[row][col] == piece:
                    count += 1
                    if count == 4:
                        return True
                else:
                    break
                row += dr
                col += dc
            return False
        
        for r in range(self.rows):
            for c in range(self.columns):
                if self.grid[r][c] == piece:
                    if check_direction(r, c, 1, 0) or check_direction(r, c, 0, 1) or \
                       check_direction(r, c, 1, 1) or check_direction(r, c, 1, -1):
                        return True
        return False
    