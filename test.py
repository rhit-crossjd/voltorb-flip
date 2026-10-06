import numpy as np
from voltorb import voltorb
from game import Game

def test():
    board = np.full((5, 5), "*", str)
    rows = [4, 7, 2, 7, 5]
    row_orbs = [1, 0, 3, 2, 0]
    cols = [4, 5, 6, 6, 4]
    col_orbs = [3, 0, 1, 1, 1]
    game = Game(board, rows, row_orbs, cols, col_orbs, False)
    voltorb(game)
    print(game)

def test2():
    board = np.full((1, 5), "*", str)
    rows = [3]
    row_orbs = [4]
    cols = [3, 0, 0, 0, 0]
    col_orbs = [0, 1, 1, 1, 1]
    game = Game(board, rows, row_orbs, cols, col_orbs, True)
    voltorb(game)
    print(game)

def test3():
    board = np.full((1, 5), "*", str)
    rows = [3]
    row_orbs = [3]
    cols = [2, 2, 0, 0, 0]
    col_orbs = [0, 0, 1, 1, 1]
    game = Game(board, rows, row_orbs, cols, col_orbs, True)
    voltorb(game)
    print(game)

def test4():
    board = np.full((1, 5), "*", str)
    rows = [11]
    row_orbs = [1]
    cols = [2, 3, 3, 3, 0]
    col_orbs = [0, 0, 0, 0, 1]
    game = Game(board, rows, row_orbs, cols, col_orbs, True)
    voltorb(game)
    print(game)

def test5():
    board = np.full((5, 5), "*", str)
    rows = [6, 4, 7, 5, 3]
    row_orbs = [1, 1, 0, 3, 2]
    cols = [1, 6, 6, 8, 4]
    col_orbs = [4, 2, 0, 0, 1]
    game = Game(board, rows, row_orbs, cols, col_orbs, True)
    voltorb(game)
    print(game)

def test6():
    board = np.full((5, 5), "*", str)
    rows = [2, 6, 5, 7, 4]
    row_orbs = [3, 0, 1, 0, 3]
    cols = [8, 3, 7, 3, 3]
    col_orbs = [0, 2, 0, 2, 3]
    game = Game(board, rows, row_orbs, cols, col_orbs, True)
    voltorb(game)
    print(game)

def test7():
    board = np.full((5, 5), "*", str)
    rows = [4, 6, 6, 4, 4]
    row_orbs = [2, 1, 0, 2, 2]
    cols = [8, 4, 1, 5, 6]
    col_orbs = [0, 1, 4, 1, 1]
    game = Game(board, rows, row_orbs, cols, col_orbs, True)
    voltorb(game)
    print(game)

test7()