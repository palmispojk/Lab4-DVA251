import sys
import math


def action(board):
    #valid = []
    #for x in board:
    #    if board[x] > 0 and x < 6:
    #        valid.append(x)
    #return valid


    action_list = board[x for x in board if board[x] > 0 and x < 6]
    return action_list



def eval(board):








def max_func(board, alfa, beta, d):
    if d == 3 or sum(board[0:6]) == 0 or sum(board[7:13]) == 0:
        return eval(state)
    v = -sys.maxsize - 1
    for a in action(board):
        placed_board = place(board, a)
        free_turn = placed_board[1]
        if free_turn:
            v = min(v, max_func(placed_board[0], alfa, beta, d+1))
            if v <= alfa:
                return v
            beta = min(beta, v)
        else:
            v = max(v, min_func(placed_board[0], alfa, beta, d+1))
            if v >= beta:
                return v
            alfa = max(alfa, v)
    return v


def min_func(board, alfa, beta, d):
    if d == 3 or sum(board[0:6]) == 0 or sum(board[7:13]) == 0:
        return eval(state)    
    v = sys.maxsize
    
    for a in action(board):
        placed_board = place(board, a)
        free_turn = placed_board[1]
        if free_turn:
            v = max(v, min_func(placed_board[0], alfa, beta, d+1))
            if v >= beta:
                return v
            alfa = max(alfa, v)
        else:
            v = min(v, max_func(placed_board[0], alfa, beta, d+1))
            if v <= alfa:
                return v
            beta = min(beta, v)
    return v




def place(board, ind):
    pieces = board[ind]
    free = False
        board[ind] = 0
        place = ind + 1
        for diff in range(pieces):
            if place > 13:
                place = 0
            board[place] += 1
            place += 1
    if place == 6:
        free = True
    if place == 14:
        place = 0
        if board[place] == 1 and place not in [6, 13]:
            steal = board[12 - place]
            board[12 - place] = 0
            if 
    return (board, free)

def min_max(board):
