
import sys
import os

# Double the backslashes to escape them properly
project_path = os.path.abspath('C:\\Users\\HP\\Desktop\\dev\\fun\\advent_of_code')
sys.path.append(project_path)

from helpers import open_file


data = open_file(r'C:\Users\HP\Desktop\dev\fun\advent_of_code\2024\day_3\input.txt')
# data = open_file(r'C:\Users\HP\Desktop\dev\fun\advent_of_code\2024\day_3\test_input.txt')

import re

operations = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)
total_value = 0

for operation in operations:
    nums = operation[4:-1]
    nums = nums.split(',')

    num1 = int(nums[0])
    num2 = int(nums[1])
    
    total_value += num1 * num2

total_value