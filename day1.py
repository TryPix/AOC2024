"""
AOC 2024 - Day 1
"""

import pandas as pd
import numpy as np

file_name = 'inputs/1.txt'

df = pd.read_csv(file_name, header=None, names=['list1', 'list2'], sep='   ')

list1 = sorted(df['list1'].tolist())
list2 = sorted(df['list2'].tolist())

ans = sum(abs(np.array(list1) - np.array(list2)))

print(ans)


ans2 = 0

for val, cnt in df['list2'].value_counts().items():
    if val in list1: ans2 += val * cnt

print(ans2)


