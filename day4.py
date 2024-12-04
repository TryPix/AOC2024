"""AOC Day 4"""

import re

file_name = "inputs/4.txt"

with open(file_name) as f:
    text = f.read()

lines = text.split('\n')[:-1]

ans = 0
ans2 = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):

        if (i < len(lines)-2 and j < len(lines[i])-2):
            if lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] in ('MAS', 'SAM'):
                if lines[i][j+2] + lines[i+1][j+1] + lines[i+2][j] in ('MAS', 'SAM'):
                    ans2 += 1

        if (j < len(lines[i])-3):
            if lines[i][j] + lines[i][j+1] + lines[i][j+2] + lines[i][j+3] in ('XMAS', 'SAMX'):
                ans += 1

        if (i < len(lines)-3):
            if lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j] in ('XMAS', 'SAMX'):
                ans += 1
        
        if (i < len(lines)-3 and j < len(lines[i])-3):
            if lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3] in ('XMAS', 'SAMX'):
                ans += 1
        
        if (i < len(lines)-3 and j >= 3):
            if lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3] in ('XMAS', 'SAMX'):
                ans += 1


print(ans)
print(ans2)
