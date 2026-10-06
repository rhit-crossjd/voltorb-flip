import numpy as np
from game import Game
from rules import no_voltorb, one_number, only_voltorb, t_compared_to_n, too_high_for_ones, total_n, total_n_plus_one

def voltorb(game: Game):
    # game.next = 2, 3
    prev = None
    while not np.array_equal(game.board, prev):
        prev = game.board.copy()
        if apply_rule(game, no_voltorb): break
        if apply_rule(game, only_voltorb): break
        if apply_rule(game, total_n): break
        if apply_rule(game, one_number): break
        if apply_rule(game, total_n_plus_one): break
        if apply_rule(game, too_high_for_ones): break
        if apply_rule(game, t_compared_to_n): break
    # if not game.is_valid(): # need for depth-first seach in case of rule failure
    for i, r in enumerate(game.rows):
        for j, c in enumerate(game.cols):
            if (2 in game.cases[i][j] or 3 in game.cases[i][j]) and not 0 in game.cases[i][j]: game.next.append((i, j))
    

def apply_rule(game: Game, rule: function):
    rule(game)
    update_game(game)
    if game.is_valid():
        return True
    return False

def update_game(game: Game):
    sync_board_cases(game)
    orbs = (game.board == "0")
    points = np.where(np.isin(game.board, ["1", "2", "3"]), game.board, "0").astype(int)
    game.cur_row_orbs = np.asarray(game.row_orbs) - orbs.sum(axis=1)
    game.cur_col_orbs = np.asarray(game.col_orbs) - orbs.sum(axis=0)
    game.cur_rows = np.asarray(game.rows) - points.sum(axis=1)
    game.cur_cols = np.asarray(game.cols) - points.sum(axis=0)
    sync_board_cases(game)
    if game.debug: print(game)

def sync_board_cases(game: Game):
    for i in range(len(game.rows)):
        for j in range(len(game.cols)):
            cell = game.cases[i][j]
            if len(cell) == 1: game.board[i][j] = str(cell[0])
            val = game.board[i][j]
            if val in {"0", "1", "2", "3"}: game.cases[i][j] = [int(val)]