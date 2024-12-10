"""AOC day 10"""

from collections import defaultdict, deque


file_name = "inputs/10.txt"

with open(file_name) as f:
    text = f.read().split('\n')[:-1]

lines = []
for i in text:
    line = list(map(int, list(i)))
    line.append(-2)
    line.insert(0, -2)
    lines.append(line)

lines.append([-2 for _ in range(len(line))])
lines.insert(0, [-2 for _ in range(len(line))])

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = len(lines)
m = len(lines[0])


adj = {i : [] for i in range(0, n*m)}

for i in range(1, n-1):
    for j in range(1, m-1):
        for dir in dirs:
            if lines[i + dir[0]][j + dir[1]] - lines[i][j] == 1:
                adj[i*m+j].append((i + dir[0]) * m + (j + dir[1]))

starts = []
ends = []
for i in range(1, n-1):
    for j in range(1, m-1):
        if lines[i][j] == 0:
            starts.append(i*m + j)
        if lines[i][j] == 9:
            ends.append(i*m + j)


def bfs(s, t, adj):
    visited = []
    count = []

    dist = defaultdict(lambda: float('inf'))
    count = defaultdict(int)

    visited.append(s)

    dist[start] = 0
    count[start] = 1

    queue = deque([start])

    while queue:
        u = queue.popleft()

        for v in adj[u]:
            if dist[v] > dist[u] + 1:
                dist[v] = dist[u] + 1
                count[v] = count[u]
                queue.append(v)
            elif dist[v] == dist[u] + 1:
                count[v] += count[u]

            # if v not in visited:
            #     visited.append(v)
            #     queue.append(v)
    
    return count[t]

ans = 0
for start in starts:
    for end in ends:
        ans += bfs(start, end, adj)

print(ans)
