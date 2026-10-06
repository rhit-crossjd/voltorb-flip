import numpy as np
from game import Game

def no_voltorb(game: Game):
    if game.debug: print("RULE: NO_VOLTORB")
    row_orbs = np.asarray(game.cur_row_orbs)
    col_orbs = np.asarray(game.cur_col_orbs)
    row_clear = row_orbs == 0
    col_clear = col_orbs == 0
    clear_mask = row_clear[:, None] | col_clear[None, :]
    for r, c in zip(*np.nonzero(clear_mask)):
        no_voltorb_square(game, r, c)

def only_voltorb(game: Game):
    if game.debug: print("RULE: ONLY_VOLTORB")
    unknown = np.strings.count(game.board, "*")
    row_orbs = np.asarray(game.cur_row_orbs)
    col_orbs = np.asarray(game.cur_col_orbs)
    row_bomb = (row_orbs == unknown.sum(axis=1)) & (row_orbs != 0)
    col_bomb = (col_orbs == unknown.sum(axis=0)) & (col_orbs != 0)
    bomb_mask = ((row_bomb[:, None]) | (col_bomb[None, :])) & unknown
    for r, c in zip(*np.nonzero(bomb_mask)):
        only_voltorb_square(game, r, c)

def total_n(game: Game):
    if game.debug: print("RULE: TOTAL_N")
    unknown = np.strings.count(game.board, "*")
    rows = np.asarray(game.cur_rows)
    cols = np.asarray(game.cur_cols)
    row_orbs = np.asarray(game.cur_row_orbs)
    col_orbs = np.asarray(game.cur_col_orbs)
    row_check = rows + row_orbs == unknown.sum(axis=1)
    col_check = cols + col_orbs == unknown.sum(axis=0)
    mask = row_check[:, None] | col_check[None, :]
    for r, c in zip(*np.nonzero(mask)):
        total_n_square(game, r, c)

def one_number(game: Game):
    if game.debug: print("RULE: ONE_NUMBER")
    unknown = np.strings.count(game.board, "*")
    row_orbs = np.asarray(game.cur_row_orbs)
    col_orbs = np.asarray(game.cur_col_orbs)
    row_check = 1 + row_orbs == unknown.sum(axis=1)
    col_check = 1 + col_orbs == unknown.sum(axis=0)
    mask = row_check[:, None] | col_check[None, :]
    for r, c in zip(*np.nonzero(mask)):
        if (row_check[r]): one_num_square(game, r, c, game.cur_rows[r])
        if (col_check[c]): one_num_square(game, r, c, game.cur_cols[c])

def total_n_plus_one(game: Game):
    if game.debug: print("RULE: TOTAL_N_PLUS_ONE")
    unknown = np.strings.count(game.board, "*")
    rows = np.asarray(game.cur_rows)
    cols = np.asarray(game.cur_cols)
    row_orbs = np.asarray(game.cur_row_orbs)
    col_orbs = np.asarray(game.cur_col_orbs)
    row_check = rows + row_orbs == unknown.sum(axis=1) + 1
    col_check = cols + col_orbs == unknown.sum(axis=0) + 1
    mask = row_check[:, None] | col_check[None, :]
    for r, c in zip(*np.nonzero(mask)):
        total_n_plus_one_square(game, r, c)

def too_high_for_ones(game: Game):
    if game.debug: print("RULE: TOO_HIGH_FOR_ONES")
    unknown = np.strings.count(game.board, "*")
    rows = np.asarray(game.cur_rows)
    cols = np.asarray(game.cur_cols)
    row_orbs = np.asarray(game.cur_row_orbs)
    col_orbs = np.asarray(game.cur_col_orbs)
    row_check = (rows + 1) / 3 >= unknown.sum(axis=1) - row_orbs
    col_check = (cols + 1) / 3 >= unknown.sum(axis=0) - col_orbs
    mask = row_check[:, None] | col_check[None, :]
    for r, c in zip(*np.nonzero(mask)):
        too_high_for_ones_square(game, r, c)

def t_compared_to_n(game: Game):
    if game.debug: print("RULE: T_COMPARED_TO_N")
    unknown = np.strings.count(game.board, "*")
    rows = np.asarray(game.cur_rows)
    cols = np.asarray(game.cur_cols)
    row_orbs = np.asarray(game.cur_row_orbs)
    col_orbs = np.asarray(game.cur_col_orbs)
    R_N = (unknown.sum(axis=1) - row_orbs)
    C_N = (unknown.sum(axis=0) - col_orbs)
    rows_ones_check = rows < (2 * R_N)
    rows_twos_check = rows % 2 != R_N % 2
    rows_threes_check = rows > (2 * R_N)
    cols_ones_check = cols < (2 * C_N)
    cols_twos_check = cols % 2 != C_N % 2
    cols_threes_check = cols > (2 * C_N)
    # print(rows_ones_check) # -> at least 2N-T 1's
    # print(2*R_N - rows)
    # print(rows_twos_check) # -> at least one 2
    # print(rows_threes_check) # -> at least T-2N 3's
    # print(rows - 2*R_N)
    # print(cols_ones_check) # -> at least 2N-T 1's
    # print(2*C_N - cols)
    # print(cols_twos_check) # -> at least one 2
    # print(cols_threes_check) # -> at least T-2N 3's
    # print(cols - 2*C_N)
    ones_candidates = np.array([[1 in cell for cell in row] for row in game.cases]) & unknown
    twos_candidates = np.array([[2 in cell for cell in row] for row in game.cases]) & unknown
    threes_candidates = np.array([[3 in cell for cell in row] for row in game.cases]) & unknown
    ones_row_hit = rows_ones_check & (ones_candidates.sum(axis=1) == 2 * R_N - rows)
    ones_col_hit = cols_ones_check & (ones_candidates.sum(axis=0) == 2 * C_N - cols)
    twos_row_hit = rows_twos_check & (twos_candidates.sum(axis=1) == 1)
    twos_col_hit = cols_twos_check & (twos_candidates.sum(axis=0) == 1)
    threes_row_hit = rows_threes_check & (threes_candidates.sum(axis=1) == rows - 2 * R_N)
    threes_col_hit = cols_threes_check & (threes_candidates.sum(axis=0) == cols - 2 * C_N)
    ones = (ones_row_hit[:, None] | ones_col_hit[None, :]) & ones_candidates
    twos = (twos_row_hit[:, None] | twos_col_hit[None, :]) & twos_candidates
    threes = (threes_row_hit[:, None] | threes_col_hit[None, :]) & threes_candidates
    for r, c in zip(*np.nonzero(ones)):
        t_compared_to_n_square(game, r, c, 1)
    for r, c in zip(*np.nonzero(twos)):
        t_compared_to_n_square(game, r, c, 2)
    for r, c in zip(*np.nonzero(threes)):
        t_compared_to_n_square(game, r, c, 3)


def no_voltorb_square(game: Game, r: int, c: int):
    cell = game.cases[r][c]
    if 0 in cell and len(game.cases[r][c]) != 1: cell.remove(0)

def only_voltorb_square(game: Game, r: int, c: int):
    game.cases[r][c] = [0]

def total_n_square(game: Game, r: int, c: int):
    cell = game.cases[r][c]
    if 2 in cell and len(game.cases[r][c]) != 1: cell.remove(2)
    if 3 in cell and len(game.cases[r][c]) != 1: cell.remove(3)

def one_num_square(game: Game, r: int, c: int, val: int):
    cell = game.cases[r][c]
    if 1 in cell and len(game.cases[r][c]) != 1 and val != 1: cell.remove(1)
    if 2 in cell and len(game.cases[r][c]) != 1 and val != 2: cell.remove(2)
    if 3 in cell and len(game.cases[r][c]) != 1 and val != 3: cell.remove(3)

def total_n_plus_one_square(game: Game, r: int, c: int):
    cell = game.cases[r][c]
    if 3 in cell and len(game.cases[r][c]) != 1: cell.remove(3)

def too_high_for_ones_square(game: Game, r: int, c: int):
    cell = game.cases[r][c]
    if 1 in cell and len(game.cases[r][c]) != 1: cell.remove(1)

def t_compared_to_n_square(game: Game, r: int, c: int, val: int):
    if game.cases[r][c] != [val]: game.cases[r][c]= [val]