"""
AOC - day 2
"""

file_name = "inputs/2.txt"

def is_safe(list):
    isDec = all(i < j for i, j in zip(list, list[1:]))
    isInc = all(i > j for i, j in zip(list, list[1:]))

    gap = all(abs(i-j) > 0 and abs(i-j) <= 3 for i, j in  zip(list, list[1:]))

    if not (isInc or isDec): return 0
    if gap: return True

    return False

def is_very_safe(list):
    if is_safe(list): return True

    for i in range(len(list)):
        s = is_safe(list[:i] + list[i+1:])
        if s: return True
    return False


with open(file_name) as f:
    lines = f.readlines()

ans = 0
ans2 = 0
for line in lines:
    split_line = list(map(int, line.split()))
    if (is_safe(split_line)): ans += 1
    if (is_very_safe(split_line)): ans2 +=1

print(ans)
print(ans2)
