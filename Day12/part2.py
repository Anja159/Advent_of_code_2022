#!/usr/bin/python3
from collections import deque

a = []

f = open("in.txt", "r")
for vrstica in f:
    a.append(vrstica.strip())

grid = [[0 for i in range(len(a[0]))] for j in range(len(a))]

for r in range(len(a)):
    for c in range(len(a[0])):
        if a[r][c]=='S':
            grid[r][c] = 1
        elif a[r][c] == 'E':
            grid[r][c] = 26
        else:
            grid[r][c] = ord(a[r][c]) - 96

# Building qeue
vrsta = deque()
for r in range(len(a)):
    for c in range(len(a[1])):
        if (grid[r][c] == 1):
            vrsta.append(((r,c), 0))

# BFS
xy = [(-1,0),(0,1),(1,0),(0,-1)]
prev = set()
while vrsta:
    (r,c),d = vrsta.popleft()
    if not (r,c) in prev:
        if a[r][c]=='E':
            print(d)
        prev.add((r,c))

        for dr,dc in xy:
            ena = r+dr
            dva = c+dc
            if 0<=ena<len(a) and 0<=dva<len(a[1]) and grid[ena][dva]<=grid[r][c]+1:
                vrsta.append(((ena,dva),d+1))
