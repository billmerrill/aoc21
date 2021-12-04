from io import StringIO
import re
import numpy


HIGH_MARK = 999
WINNER = HIGH_MARK * 5

def load_input():
    fh = open('input.txt', 'r')
    plays_tmp = fh.readline()
    plays = [int(x) for x in plays_tmp.split(',')]

    boards = []
    while(tmp := fh.readline()):
        if (len(tmp) > 1):
            txt = tmp
            for i in range(4):
                tmp = fh.readline()
                txt = txt + tmp
            board = numpy.loadtxt(StringIO(txt), dtype=int)
            boards.append(board)

    return plays, boards

def mark(board, play):
    return numpy.where(board == play, HIGH_MARK, board)

def did_board_win(board):
    for i in range(5):
        if numpy.sum(board[i,:]) == WINNER:
            return True
        if numpy.sum(board[:,i]) == WINNER:
            return True
    return False

def play(plays, boards):
    while(len(boards) > 0 and plays):
        to_del = []
        play = plays.pop(0)
        for j, board in enumerate(boards):
            boards[j] = mark(board, play)
            if did_board_win(boards[j]):
                if len(boards) == 1:
                    return(boards[0], play)
                if len(boards) - len(to_del) > 1:
                    to_del.append(j)

        while(to_del):
            del(boards[to_del.pop()])

plays, boards = load_input()
win_board, win_play = play(plays, boards)
flat = win_board.flatten()
unmarked_sum = numpy.sum(flat[flat[:]<HIGH_MARK])
print('unmarked sum=', unmarked_sum)
print('winning play', win_play)
print(unmarked_sum * win_play)


