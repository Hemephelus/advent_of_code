
import sys
import os

# Double the backslashes to escape them properly
project_path = os.path.abspath('C:\\Users\\HP\\Desktop\\dev\\fun\\advent_of_code')
sys.path.append(project_path)

from helpers import txt_to_D_list

reports = txt_to_D_list(r'C:\Users\HP\Desktop\dev\fun\advent_of_code\2024\day_2\input.txt')
# reports = txt_to_D_list(r'C:\Users\HP\Desktop\dev\fun\advent_of_code\2024\day_2\test_input.txt')
total_safe = 0
for report in reports:
    levels = report.split(' ')
    new_levels = levels
    counter = 0
    safe = True

    print('before', levels, safe)
    for i in range(len(levels)+1):
        safe = True
        growth = []
        for j in range(len(new_levels)-1):
            level_a = int(new_levels[j])
            level_b = int(new_levels[j+1])


            diff = (level_a - level_b)
            g = diff > 0

            if abs(diff) > 3 or abs(diff) < 1:
                safe = False
                break

            if len(growth) == 0:
                growth.append(g)
                continue

            if g != growth[-1]:
                safe = False
                break

        if safe:
            break

        
        new_levels = levels[0:i] + levels[i+1:]
    # print('after', levels, safe)
        print('levels', new_levels)
        
    


    if safe:
      total_safe += 1
    


print(total_safe)
