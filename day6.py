"""AOC day 6"""

file_name = "inputs/6.txt"

with open(file_name) as f:
    text = f.read().split('\n')

grid = text
for i in range(len(text)-1):
    grid[i] = list(text[i])
    grid[i].insert(0, 'O')
    grid[i].append('O')
    if '^' in grid[i]: pos = [i, grid[i].index('^')] 

grid[-1] = ['O' for i in range(len(grid[0]))]
grid.insert(0, ['O' for i in range(len(grid[0]))])
start = pos

dir = [-1, 0]

visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

while True:

    if (grid[pos[0]][pos[1]] == 'O'): break

    visited[pos[0]][pos[1]] = True

    while (grid[pos[0] + dir[0]][pos[1] + dir[1]] == '#'):
        if dir == [-1, 0]: dir = [0, 1]
        elif dir == [0, 1]: dir = [1, 0]
        elif dir == [1, 0]: dir = [0, -1]
        else: dir = [-1, 0]
    
    pos = [pos[0] + dir[0], pos[1] + dir[1]]
    

print(sum([row.count(True) for row in visited]))

visited_pos = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if visited[i][j] == True]

ans = 0

for (i, j) in visited_pos:

    dir = [-1, 0]
    pos = start
    directions = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]

    if [i, j] == start: continue
    if grid[i][j] == '#': continue

    grid[i][j] = '#' # block

    is_cycle = False

    while True:

        if (grid[pos[0]][pos[1]] == 'O'):
            break
        
        if (dir in directions[pos[0]][pos[1]]):
            is_cycle = True
            break

        directions[pos[0]][pos[1]].append(dir)

        while (grid[pos[0] + dir[0]][pos[1] + dir[1]] == '#'):
            if dir == [-1, 0]: dir = [0, 1]
            elif dir == [0, 1]: dir = [1, 0]
            elif dir == [1, 0]: dir = [0, -1]
            else: dir = [-1, 0]
        
        pos = [pos[0] + dir[0], pos[1] + dir[1]]

    grid[i][j] = '.' # unblock

    if is_cycle:
        ans += 1


print(ans)


