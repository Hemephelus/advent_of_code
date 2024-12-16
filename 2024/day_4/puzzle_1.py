
import sys
import os

# Double the backslashes to escape them properly
project_path = os.path.abspath('C:\\Users\\HP\\Desktop\\dev\\fun\\advent_of_code')
sys.path.append(project_path)

from helpers import open_file


data = open_file(r'C:\Users\HP\Desktop\dev\fun\advent_of_code\2024\day_4\input.txt')
# data = open_file(r'C:\Users\HP\Desktop\dev\fun\advent_of_code\2024\day_4\test_input.txt')

