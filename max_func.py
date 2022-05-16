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
    return (random.randint(0, 10), 0)







def max_func(board, alfa, beta, d):
    c_board = copy.deepcopy(board)
    if d == 3 or sum(c_board[0:6]) == 0 or sum(c_board[7:13]) == 0:
        return eval(c_board)
    v = -sys.maxsize - 1
    for a in action(c_board):
        print(c_board)
        placed_board = place(c_board, a)
        print(placed_board)
        free_turn = placed_board[1]
        if free_turn:
            v = max(v, max_func(placed_board[0], alfa, beta, d+1)[0])
            if v <= alfa:
                print(v, a)
                return (v, a)
            beta = min(beta, v)
        else:
            v = max(v, min_func(placed_board[0], alfa, beta, d+1)[0])
            if v >= beta:
                print(v, a)
                return (v, a)
            alfa = max(alfa, v)
    return (v, 0)


def min_func(board, alfa, beta, d):
    c_board = copy.deepcopy(board)
    if d == 3 or sum(c_board[0:6]) == 0 or sum(c_board[7:13]) == 0:
        return eval(c_board)    
    v = sys.maxsize
    
    for a in action(c_board):
        print(c_board)
        placed_board = place(c_board, a)
        print(placed_board)
        free_turn = placed_board[1]
        if free_turn:
            v = min(v, min_func(placed_board[0], alfa, beta, d+1)[0])
            if v >= beta:
                print(v, a)
                return (v, a)
            alfa = max(alfa, v)
        else:
            v = min(v, max_func(placed_board[0], alfa, beta, d+1)[0])
            if v <= alfa:
                print(v, a)
                return (v, a)
            beta = min(beta, v)
    return (v, 0)




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


def min_max(board):
    c_board = copy.deepcopy(board)
    v = max_func(c_board, -sys.maxsize - 1, sys.maxsize, 1)
    print(board)
    print(v[1])
    return v[1]




def main():
    #check all functions
    #steal and place
    steal_board = [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0]
    print(steal_board)
    print(place(steal_board, 0))


    #

if __name__ == "__main__":
    main()
