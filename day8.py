"""AOC day 8"""

file_name = "inputs/8.txt"

with open(file_name) as f:
    text = f.read().split('\n')[:-1]

def is_in_range(n, m, i, j):
    return i < n and i >= 0 and j < m and j >= 0

lines = []
for l in text:
    lines.append(list(l))

antennas = {}

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '.': continue
        if lines[i][j] in antennas:
            antennas[lines[i][j]].append((i, j))
        else:
            antennas[lines[i][j]] = [(i, j)]

antinodes = set()
n = len(lines)
m = len(lines[0])
for atype, positions in antennas.items():
    for i in range(len(positions)-1):
        for j in range(i+1, len(positions)):
            posA = positions[i]
            posB = positions[j]
            row_diff = posB[0] - posA[0]
            col_diff = posB[1] - posA[1]

            a1 = (posA[0], posA[1])
            a2 = (posB[0], posB[1])

            while is_in_range(n, m, a1[0], a1[1]) or is_in_range(n, m, a2[0], a2[1]):

                if is_in_range(n, m, a1[0], a1[1]): antinodes.add(a1)
                if is_in_range(n, m, a2[0], a2[1]): antinodes.add(a2)

                # only take these for part 1, checking if in range
                a1 = (a1[0] - row_diff, a1[1] - col_diff)
                a2 = (a2[0] + row_diff, a2[1] + col_diff)

print(len(antinodes))


