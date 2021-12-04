import re

import numpy

WINNER = 999 * 5

def load_input():
    boards = []
    fh = open('input.txt', 'r')
    plays_tmp = fh.readline()
    plays = [int(x) for x in plays_tmp.split(',')]

    pattern = r'\s*' + r'(\S+)\s*' * 5

    board = numpy.ndarray(shape=(5,5), dtype=int)
    cur_line = 0
    while(tmp := fh.readline()):
        if (len(tmp) == 1):
            cur_line = 0
            board = numpy.ndarray(shape=(5,5), dtype=int)
        elif (len(tmp) > 1):
            board[cur_line] = list(map(int,(re.search(pattern, tmp).groups())))
            if cur_line == 4:
                boards.append(board)
                cur_line = 0
            else:
                cur_line += 1

    return plays, boards

def mark(board, play):
    return numpy.where(board == play, 999, board)



def did_board_win(board):
    for i in range(5):
        if numpy.sum(board[i,:]) == WINNER:

            return True
        if numpy.sum(board[:,i]) == WINNER:
            return True
    return False

def play(plays, boards):
    for play in plays:
        print(play)
        for j, board in enumerate(boards):
            boards[j] = mark(board, play)
            if did_board_win(boards[j]):
                print("winner", boards[j])
                return boards[j], play



plays, boards = load_input()
win_board, win_play = play(plays, boards)
flat = win_board.flatten()
unmarked_sum = numpy.sum(flat[flat[:]<999])
print('unmarked sum=', unmarked_sum)
print('winning play', win_play)
print(unmarked_sum * win_play)


