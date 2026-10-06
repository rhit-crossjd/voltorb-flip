import numpy as np

class Game:
    def __init__(
        self, 
        board: np.ndarray,
        rows: list[int], 
        row_orbs: list[int], 
        cols: list[int], 
        col_orbs: list[int],
        debug: True
    ):
        self.board = board
        self.rows = rows
        self.cur_rows = rows.copy()
        self.row_orbs = row_orbs
        self.cur_row_orbs = row_orbs.copy()
        self.cols = cols
        self.cur_cols = cols.copy()
        self.col_orbs = col_orbs
        self.cur_col_orbs = col_orbs.copy()
        self.cases = [[[0, 1, 2, 3] for _ in cols] for _ in rows]
        self.next = []
        self.next_index = 0
        self.debug = debug

    def __str__(self):
        string=""
        guess_row, guess_col = self.next[self.next_index] if len(self.next) > 0 else (-1, -1)
        if self.debug:
            for row_index, row in enumerate(self.board):
                string+="["
                for col_index, col in enumerate(row):
                    string += f' \033[32m[{col}]\033[0m   ' if guess_row == row_index and guess_col == col_index else f'  {col}    '
                string += f'{self.rows[row_index]}/{self.row_orbs[row_index]}    '
                string += f'{self.cur_rows[row_index]}/{self.cur_row_orbs[row_index]}]\n'
            string+="["
            for index, _ in enumerate(self.cols):
                string += f' {self.cols[index]}/{self.col_orbs[index]} '
                if index != len(self.cols)-1: string += "  "
                else: string+="]\n["
            for index, _ in enumerate(self.cur_cols):
                string += f' {self.cur_cols[index]}/{self.cur_col_orbs[index]} '
                if index != len(self.cur_cols)-1: string += "  "
                else: string += "]\n\n"
        for i, row in enumerate(self.rows):
            string+="[ "
            for j, col in enumerate(self.cols):
                string += f'\033[32m{str(self.cases[i][j])}\033[0m' if guess_row == i and guess_col == j else str(self.cases[i][j])
                string += " " * 3 * (4 - len(self.cases[i][j]))
                string = string[:-2] if len(self.cases[i][j]) == 0 else string
                if j < len(self.cols)-1: string += "  "
                else: string+=" ]\n"
            if i == len(self.rows)-1: string = string[:-1]
        return string

    def is_valid(self) -> bool:
        for r in self.board:
            for c in r: 
                if c == "*": return False
        for r in self.cur_rows:
            if r != 0: return False
        for c in self.cur_cols:
            if c != 0: return False
        for r in self.cur_row_orbs:
            if r < 0: return False
        for c in self.cur_col_orbs:
            if c < 0: return False
        return True