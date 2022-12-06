#!/usr/bin/python
f = open("in.txt", "r").read()
n = 14

for i in range(0, len(f) - n):
    t = 0
    for h in range(0, n):
        for r in range(h + 1, n):
            if f[i + h] == f[i + r]:
                t = 1
    if t == 0:
        print(i + n)
        break