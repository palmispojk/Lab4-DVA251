import sys
import math
import copy
import random




def action(board):
    #valid = []
    #for x in board:
    #    if board[x] > 0 and x < 6:
    #        valid.append(x)
    #return valid

    action_list = [i for i, e in enumerate(board) if e > 0 and i < 6]
    for i, e in enumerate(board):
        if e == 0 and i < 6:
            print(i, action_list)

    return action_list


def eval(board):
    return random.randint(0, 10)





def place(board, ind):
    pieces = board[ind]
    board[ind] = 0
    free = False
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
        board[6] += steal
    return (board, free)

