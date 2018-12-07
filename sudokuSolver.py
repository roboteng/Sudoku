from sudoku import *
import numpy as np

def solve(board): #board.board[y][x]
    def next_pos(cur):
        x = cur[0]
        y = cur[1]
        x += 1
        if x >= 9:
            x = 0
            y += 1
        while not board.mutable[y][x]:
            x += 1
            if x >= 9:
                x = 0
                y += 1
        return (x,y)

    def prev_pos(cur):
        x = cur[0]
        y = cur[1]
        x -= 1
        if x < 0:
            x = 8
            y -= 1
        while not board.mutable[y][x]:
            x -= 1
            if x < 0:
                x = 8
                y -= 1
        return (x,y)

    cursor = next_pos((-1,0))
    print(cursor)
    print(board)
    num = 0
    while not board.is_filled():
        num += 1
        #print(cursor)
        board.board[cursor[1]][cursor[0]] += 1
        while not board.spot_check(cursor[0],cursor[1]):
            board.board[cursor[1]][cursor[0]] += 1
        if not num % 1000:
            print(num)
            print(board)
        if board.board[cursor[1]][cursor[0]] > 9:
            board.board[cursor[1]][cursor[0]] = 0
            cursor = prev_pos(cursor)
        else:
            cursor = next_pos(cursor)
        
        if num > 2000000:
            break
    
    return board

    
sudoku = SudokuBoard('Puzzles/sudoku1.txt')
print(sudoku)

sudoku = solve(sudoku)

print(sudoku)
