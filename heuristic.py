from utils import *
from random import randint


def compute_utility(state):
    x = 0
    if state.utility != 0:
        return state.utility * 10000000000000
    for move in state.moves:
        x -= (calculateValue(state.board, move, state.to_move, (0, 1)) +
              calculateValue(state.board, move, state.to_move, (1, 0)) +
              calculateValue(state.board, move, state.to_move, (1, -1)) +
              calculateValue(state.board, move, state.to_move, (1, 1)))
        player = if_(state.to_move == 'X', 'O', 'X')
        x += (calculateValue(state.board, move, player, (0, 1)) +
              calculateValue(state.board, move, player, (1, 0)) +
              calculateValue(state.board, move, player, (1, -1)) +
              calculateValue(state.board, move, player, (1, 1)))
    return x


def calculateValue(board, move, player, (delta_x, delta_y)):
    x, y = move
    distancia = 1
    h = 0
    while 0 <= x <= 6 and 0 <= y <= 5:
        if board.get((x, y)) == player:
            h += 50 / distancia
        elif board.get((x, y)) is None:
            if board.get((x, y + 1)) is not None and board.get((x, y + 1)) != player:
                if board.get((x, y - 1)) is not None and board.get((x, y - 1)) != player:
                    h += 50000000
            h += 10
        else:
            h += 25 / distancia
        distancia += 5
        x, y = x + delta_x, y + delta_y
    return h


def random_heuristic(state):
    return randint(-200, 200)

