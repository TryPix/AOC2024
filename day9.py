"""AOC day 9"""

file_name = "inputs/9.txt"

with open(file_name) as f:
    text = f.read()[:-1]


string = {}
lengths = {}
spaces = {}

index = 0
for i in range(len(text)):
    l = int(text[i])
    if i % 2 == 0: 
        lengths[i // 2] = l
    else: spaces[(i-1) // 2] = l

    for j in range(0, l):
        if i % 2 == 0:
            string[index] = (i // 2)
        else:
            string[index] = '.'
        index += 1

# init_length = len(string)
# index = init_length -1
# free = 0

# for i in range(init_length-1, -1, -1):
#     while index > 0 and string[index] == '.':
#         index -= 1
#     while free < init_length and string[free] != '.':
#         free += 1
    
#     if free < index:
#         string[free] = string[index]
#         string[index] = '.'
#         free += 1
#         index -= 1

# ans = 0
# for index, value in string.items():
#     if value == '.': break
#     ans += index * value

def move(string, l, c):
    init_length = len(string)
    start = -1
    end = -1

    in_free = False

    for i in range(init_length):
        if string[i] == '.' and not in_free:
            start = i
            in_free = True
        if string[i] != '.' and in_free:
            end = i
            in_free = False
        
        if start >= 0 and end > start:
            space = end - start
            if space >= l:
                for index, value in string.items():
                    if value == c:
                        if start > index: return False
                        string[index] = '.'

                for j in range(l):
                    string[start + j] = c
                return True
    return False

n = len(lengths.keys())

for i in range(n-1, 0, -1):
    move(string, lengths[i], i)

ans = 0
for index, value in string.items():
    if value == '.': continue
    ans += index * value

print(ans)

