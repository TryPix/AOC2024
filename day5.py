"""AOC day 5"""

from functools import cmp_to_key


file_name = "inputs/5.txt"

with open(file_name) as f:
    text = f.read().split('\n')

def get_order(rules):
    before = {i: set() for i in range(10, 100)}

    for rule in rules:
        before[int(rule[0])].add(int(rule[1]))
    
    return before

def compare(x, y):
    if int(y) in before[int(x)]:
        return 1
    elif int(x) in before[int(y)]:
        return -1
    return 0

def new_list(line):
    return sorted(line, key=cmp_to_key(compare))

s1 = []
s2 = []

is1 = True
for line in text:
    if line == '':
        is1 = False
        continue
    
    if is1:
        s1.append(line.split('|'))
    else:
        s2.append(line.split(','))


ans = 0
before = get_order(s1)
ans2 = 0

for line in s2:
    isOrdered = True

    for rule in s1:
        a = int(rule[0])
        b = int(rule[1])

        if str(a) in line and str(b) in line:
            if rule.index(f'{a}') < rule.index(f'{b}'):
                if line.index(f'{b}') < line.index(f'{a}'):
                    isOrdered = False
                    break
            elif rule.index(f'{b}') < rule.index(f'{a}'):
                if line.index(f'{a}') < line.index(f'{b}'):
                    isOrdered = False
                    break
    
    if isOrdered: 
        ans += int(line[int((len(line)-1)/2)])
    
    else:
        ans2 += int(new_list(line)[int((len(line)-1)/2)])




print(ans)
print(ans2)

