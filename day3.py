"""AOC Day 3"""

import re

file_name = "inputs/3.txt"

with open(file_name) as f:
    text = f.read()


s1 = "mul+\(\d+,\d+\)"
s2 = s1 + "|do+\(\)|don't+\(\)"

valid = re.findall(s2, text)

enabled = True
ans = 0

for i in valid:
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

