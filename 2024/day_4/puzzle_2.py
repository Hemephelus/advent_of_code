
import sys
import os

# Double the backslashes to escape them properly
project_path = os.path.abspath('C:\\Users\\HP\\Desktop\\dev\\fun\\advent_of_code')
sys.path.append(project_path)

from helpers import open_file


data = open_file(r'C:\Users\HP\Desktop\dev\fun\advent_of_code\2024\day_4\input.txt')
# data = open_file(r'C:\Users\HP\Desktop\dev\fun\advent_of_code\2024\day_4\test_input.txt')


# SOLUTION
puzzle = data
words = [
    'SSMM',
'MSMS',
'MMSS',
'SMSM',
]

def is_xmas(puzzle, i, j):
    up_left = [i-1, j-1]
    down_right = [i+1, j+1]
    up_right = [i-1, j+1]
    down_left = [i+1, j-1]

    checks = [
        up_left,
        up_right ,
        down_left ,
        down_right ,
    ]

    word = ''

    for check in checks:
        
        if check[0] < 0 or check[1] < 0 or check[0] > len(puzzle)-1 or check[1] > len(puzzle[0])-1:
            break
        
        word += puzzle[check[0]][check[1]]

    if word in words:
        print(word)
        return 1
    return 0


total = 0

for i in range(len(puzzle)):
    line = puzzle[i]
    for j in range(len(line)):
        letter = line[j]
        if letter == 'A':
            
            total += is_xmas(puzzle, i, j)

print('total',total)