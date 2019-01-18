from sudoku import *
import time
import numpy as np

def solve(board): #board.board[y][x]
    if not board.is_valid():
        return -1
    def next_pos(cur):
        x = cur[0]
        y = cur[1]
        x += 1
        if x >= 9:
            x = 0
            y += 1
        while not board.mutable[y, x]:
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
    #print(cursor)
    #print(board)
    num = 0
    while True:
        num += 1
        #print(cursor)
        board.board[cursor[1]][cursor[0]] += 1
        while not board.spot_check(cursor[0],cursor[1]):
            board.board[cursor[1]][cursor[0]] += 1
##        if not num % 1000:
##            print(num)
##            print(board)
        if board.board[cursor[1]][cursor[0]] > 9:
            board.board[cursor[1]][cursor[0]] = 0
            cursor = prev_pos(cursor)
        else:
            try:
                cursor = next_pos(cursor)
            except:
                #print(num)
                #print(board)
                break
    return board

def smart_solve(board):
    board = prep(board)

    changed = False

    while True:
        changed = False
        #simplfy single cell
        for y in range(9):
            for x in range(9):
                num, l = count(board, x, y)
                if num == 1:
                    #print("at ({},{}) is only {}".format(x,y,l[0]))
                    board.board[y][x] = l[0]
                    board.mutable[y][x] = False
                    update_cell(board,x,y)
                    changed = True
                    #print("cell")
        #simplify row
        for y in range(9):
            for digit in range(1,10):
                l = []
                for i in range(9):
                    if board.possible[y, i, digit]:
                        l.append(i)
                if len(l) == 1:
                    board.board[y, l[0]] = digit
                    board.mutable[y,l[0]] = False
                    update_cell(board,l[0],y)
                    changed = True
                    #print("row")
                    
        #simplify Column
        for x in range(9):
            for digit in range(1,10):
                l = []
                for i in range(9):
                    if board.possible[i, x, digit]:
                        l.append(i)
                if len(l) == 1:
                    board.board[l[0],x] = digit
                    board.mutable[l[0], x] = False
                    update_cell(board, x, l[0])
                    changed = True
                    #print("column")
                
        if not changed:
            break
    if not board.is_filled():
        board = solve(board)
    return board

def update_cell(board, x, y):
    digit = int(board.board[y][x])
    for  i in range(9):
        #clear row
        board.possible[y][i][digit] = False
        #clear column
        board.possible[i][x][digit] = False
        #clear subsquare
        dx = i // 3
        dy = i % 3
        cx = (x // 3) * 3
        cy = (y // 3) * 3
        board.possible[cy+dy][cx+dx][digit] = False
        #clear cell
        board.possible[y][x][i+1] = False
    return board

def prep(board):
    #clear all easy options
    for x in range(9):
        for y in range(9):
            digit = board.board[y][x]
            if digit == 0: #empty cell, nothing to clear
                continue
            else:
                digit = int(digit)
            for  i in range(9):
                #clear row
                board.possible[y][i][digit] = False
                #clear column
                board.possible[i][x][digit] = False
                #clear subsquare
                dx = i // 3
                dy = i % 3
                cx = (x // 3) * 3
                cy = (y // 3) * 3
                board.possible[cy+dy][cx+dx][digit] = False
                #clear cell
                board.possible[y][x][i+1] = False
    return board

def count(board,x,y):
    counter = 0
    l = []
    for i in range(1,10):
        if board.possible[y,x,i]:
            counter += 1
            l.append(i)
    return (counter,l)

sudoku = SudokuBoard('Puzzles/sudoku3.txt')
#print(sudoku)
t = time.time()
#sudoku = solve(sudoku)
dt = time.time() - t
#print(dt)
#print(sudoku)

times = []
for i in range(50):
    i += 1
    if i < 10:
        file_name = "Puzzles/Grid_0{}.txt".format(str(i))
    else:
        file_name = "puzzles/Grid_{}.txt".format(str(i))
    puzzle = SudokuBoard(file_name)
    t = time.time()
    smart_solve(puzzle)
    dt = time.time()- t
    times.append(dt)
    print(dt)

print("Min: \t{}\nMax: \t{}\nAvg: \t{}".format(min(times),max(times),sum(times)/len(times)))
                                    
