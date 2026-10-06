import numpy as np
from voltorb import voltorb
from game import Game

def get_user_input():
    totals = input()
    val = [int(v.strip()) for v in totals.split(",")]
    if not totals or len(val) != 5:
        return
    print(val)
    return val

def main():
    board = np.full((5, 5), "*", str)
    print("Enter row totals (1, 2, 3, 4, 5)")
    rows = get_user_input()
    if not rows: return
    print("Enter row orb totals (1, 2, 3, 4, 5)")
    row_orbs = get_user_input()
    if not row_orbs: return
    print("Enter column totals (1, 2, 3, 4, 5)")
    cols = get_user_input()
    if not cols: return
    print("Enter column orb totals (1, 2, 3, 4, 5)")
    col_orbs = get_user_input()
    if not col_orbs: return
    game = Game(board, rows, row_orbs, cols, col_orbs, False)
    voltorb(game)
    revealed = set()
    while game.next_index < len(game.next):
        while tuple(game.next[game.next_index]) in revealed:
            game.next_index += 1
        print(game)
        r, c = game.next[game.next_index]
        guess = input(f"Value at ({r}, {c}) (Enter to skip): ").strip()
        revealed.add((r, c))
        if guess:
            game.board[r][c] = guess
            game.next_index = 0
            game.next = []
            voltorb(game)
        else: game.next_index += 1
        

main()