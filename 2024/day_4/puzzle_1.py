
import sys
import os

# Double the backslashes to escape them properly
project_path = os.path.abspath('C:\\Users\\HP\\Desktop\\dev\\fun\\advent_of_code')
sys.path.append(project_path)

from helpers import open_file


data = open_file(r'C:\Users\HP\Desktop\dev\fun\advent_of_code\2024\day_4\input.txt')
# data = open_file(r'C:\Users\HP\Desktop\dev\fun\advent_of_code\2024\day_4\test_input.txt')



puzzle = data

vertical_up = [
    [0, 0],
    [-1, 0],
    [-2, 0],
    [-3, 0],
]
vertical_down = [
    [0, 0],
    [1, 0],
    [2, 0],
    [3, 0],
]
horizontal_left = [
    [0, 0],
    [0, -1],
    [0, -2],
    [0, -3],
]
horizontal_right = [
  [0, 0],
    [0, 1],
    [0, 2],
    [0, 3],
]
diagonal_up_left = [
    [0, 0],
    [-1, -1],
    [-2, -2],
    [-3, -3],
]

diagonal_up_right = [
    [0, 0],
    [-1, 1],
    [-2, 2],
    [-3, 3],
]
diagonal_down_right = [
    [0, 0],
    [1, 1],
    [2, 2],
    [3, 3],
]

diagonal_down_left = [
   [0, 0],
    [1, -1],
    [2, -2],
    [3, -3],
]

def is_xmas(puzzle, i, j):
    checks = [
        vertical_down,
        vertical_up,
        horizontal_left,
        horizontal_right,
        diagonal_down_left,
        diagonal_down_right,
        diagonal_up_left,
        diagonal_up_right,
    ]

    word = 'XMAS'    
    is_valid = True
    x_count = 0

    for check in checks:
        is_valid = True
        for index, letter in enumerate(word):
            index_row = i+check[index][0]
            index_col = j+check[index][1]

            if index_col < 0 or index_row < 0 or index_row > len(puzzle)-1 or index_col > len(puzzle[0])-1:
                is_valid = False
                break

            if puzzle[index_row][index_col] != letter:
                is_valid = False
                break
        if is_valid:
            x_count += 1
    return x_count

total = 0
for i in range(len(puzzle)):
    line = puzzle[i]
    for j in range(len(line)):
        letter = line[j]
        if letter == 'X':
            total += is_xmas(puzzle, i, j)


total
