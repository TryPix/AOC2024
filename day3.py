"""AOC Day 3"""

import re

file_name = "inputs/3.txt"

with open(file_name) as f:
    text = f.read()

valid = re.findall("mul+\(\d+,\d+\)", text) # part 1
valid2 = re.findall("mul+\(\d+,\d+\)|do+\(\)|don't+\(\)", text) # part 2

enabled = True
ans = 0

for i in valid2:
    if i == 'do()': 
        enabled = True
        continue
    elif i == "don't()": 
        enabled = False
        continue

    nums = re.findall('\d+', i)
    if len(nums) < 2: print(i)
    if enabled: ans += int(nums[0]) * int(nums[1])
    

print(ans)

