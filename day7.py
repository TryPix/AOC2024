"""AOC day 7"""

file_name = "inputs/7.txt"

with open(file_name) as f:
    text = f.read().split('\n')

text = text[:-1]

sums = []
values = []
for l in text:
    index = l.find(':')
    sums.append(l[0:index])
    values.append(l[index+1:].split())

sums = list(map(int, sums))
values = [list(map(int, l)) for l in values]

ans = 0
for i in range(len(sums)):
    s = sums[i]
    v = values[i]

    dp = [0]
    for value in v:
        new = []
        for prec in dp:
            new.append(prec * value)
            new.append(prec + value)
            new.append(int(str(prec) + str(value)))
        dp = new
    
    if s in dp: 
        ans += s

print(ans)
