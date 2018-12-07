import math
import numpy as np

class SudokuBoard():
    def __init__(self, digits):
        try:
            file = open(digits)
            puzzle = file.read()
            
            puzzle_array = puzzle.split('\n')

            formatted = []
            for i in in_row():
                new_row = []
                for j in in_row():
                    new_row.append(puzzle_array[i][j])
                formatted.append(new_row)
            digits = formatted
        except:
            pass
        finally:
            '''
            Expects a 2d array of digits
            '''
            self.board = np.zeros((9,9))
            self.mutable = np.zeros((9,9))
            self.possible = np.ones((9,9,9), dtype= bool)# format will be [y][x][num]

            for i,row in enumerate(self.board):
                for j,char in enumerate(row):
                    try:
                        self.board[i][j] = int(digits[i][j])
                    except:
                        pass
                    if self.board[i][j] == 0:
                        self.mutable[i,j] = 1
        

    def __str__(self):
        result = ""
        for i,row in enumerate(self.board):
            for j,digit in enumerate(row):
                if digit == 0:
                    result += ' '
                elif digit > 9:
                    result += '*'
                else:
                    result += str(int(digit))
                if j in list(range(2,7,3)):
                    result += '|'
            result += '\n'
            if i in list(range(2,7,3)):
                result += '---+---+---\n'
        return result

    def spot_check(self,x,y):
        #row
        if SudokuBoard.has_double(self.board[:, x:x+1].flatten()):
            return False
        #column
        if SudokuBoard.has_double(self.board[y:y+1].flatten()):
            return False
        #block
        b_x = math.floor(x/3) * 3
        b_y = math.floor(y/3) * 3
        if SudokuBoard.has_double(self.board[b_y:b_y+3, b_x:b_x+3].flatten()):
            return False
        return True
    
    def is_valid(self): #check position at x,y first
        for i in range(9):
            if SudokuBoard.has_double(self.board[i:i+1].flatten()):
                return False
            if SudokuBoard.has_double(self.board[:, i:i+1].flatten()):
                return False
            s_y = (i%3)*3
            s_x = math.floor(i/3)*3
            if SudokuBoard.has_double(self.board[s_x:s_x+3, s_y:s_y+3].flatten()):
                return False
        return True

    def has_double(group):
        for i,elem in enumerate(group):
            if elem == 0:
                continue
            for check in group[i+1:]:
                if check == elem:
                    return True
        return False
    def is_filled(self):
        for row in self.board:
            for cell in row:
                if not cell:
                    return False
        return True
    
def in_row():
    for i in range(9):
        yield (i + math.floor(i/3))

if  __name__ == '__main__':
    file = open('Puzzles/sudoku1.txt')
    puzzle = file.read()
    
    puzzle_array = puzzle.split('\n')

    formatted = []
    for i in in_row():
        new_row = []
        for j in in_row():
            new_row.append(puzzle_array[i][j])
        formatted.append(new_row)

    sudoku = SudokuBoard(formatted)
    print(sudoku)

    x,y = 8,5
    sudoku.board[y][x] = 4
    print(sudoku)
    print(sudoku.spot_check(x,y))
    
