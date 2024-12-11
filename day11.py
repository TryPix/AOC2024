"""AOC day 11"""

from typing import Counter


file_name = "inputs/11.txt"

with open(file_name) as f:
    stones = list(map(int, f.read().split()))
        
old_count = Counter(stones)
for i in range(75):
    new_count = Counter()
    for stone, count in old_count.items():
        if stone == 0:
            new_count[1] += count
            continue

        length = len(str(stone))
        if length % 2 == 0: 
            ind = len(str(stone)) // 2
            s1 = int(str(stone)[:ind])
            s2 = int(str(stone)[ind:])
            new_count[s1] += count
            new_count[s2] += count
        else:
            s = stone * 2024
            new_count[s] += count
    old_count = new_count

print(sum(old_count.values()))
