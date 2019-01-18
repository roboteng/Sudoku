import re

input_str = "Puzzles/grids.txt"

input_file = open(input_str)

puzzles = input_file.read()

puzzles = puzzles.split("\n")

file_name = ""
for i,line in enumerate(puzzles):
    i_s = i % 10
    if i_s == 0:
        file_name = "Puzzles/"+ line.replace(" ", "_") + ".txt"
        f = open(file_name, mode='w')
    else:
        digits = line[:3] + "|" + line[3:6] + "|" + line[6:]
        digits = digits.replace("0", " ")
        if i_s in {3,6}:
            digits += "\n---+---+---"
        f.write(digits+ '\n')
        if i_s == 9:
            f.close()
