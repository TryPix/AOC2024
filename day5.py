"""AOC day 5"""

from functools import cmp_to_key


file_name = "inputs/5.txt"

with open(file_name) as f:
    text = f.read().split('\n')



def get_order(rules):
    before = {}

    for rule in rules:
        before[int(rule[0])] = set()
        before[int(rule[1])] = set()

    for rule in rules:
        before[int(rule[0])].add(int(rule[1]))
    
    return before

def new_list(line, before):
    max_indices = [len(line)-1 for i in line]

    for val in line:
        max_index = len(line)-1
        for other in line:
            if int(other) in before[int(val)]:
                max_index -= 1
        
        max_indices[line.index(val)] = max_index
    
    lst = [0 for i in line]
    for val in line:
        index = line.index(val)
        new_index = max_indices[index]
        lst[new_index] = val

    return lst



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
    new_order = [0 for i in line]

    for rule in s1:
        a = int(rule[0])
        b = int(rule[1])

        if str(a) in line and str(b) in line:
            if rule.index(f'{a}') < rule.index(f'{b}'):
                if line.index(f'{b}') < line.index(f'{a}'):
                    isOrdered = False
            elif rule.index(f'{b}') < rule.index(f'{a}'):
                if line.index(f'{a}') < line.index(f'{b}'):
                    isOrdered = False
    
    if isOrdered: 
        ans += int(line[int((len(line)-1)/2)])
    
    else:
        ans2 += int(new_list(line, before)[int((len(line)-1)/2)])




print(ans)
print(ans2)

