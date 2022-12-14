#!/usr/bin/env python3
ABYSS = 0
al = set()
f = open("in.txt", "r")

for line in f:
    line = line.strip()
    x = []
    for p in line.split(" -> "):
        a = p.split(",")
        x += [list(map(int, a))]

    for (x1, y1), (x2, y2) in zip(x, x[1:]):
        if (x2 < x1):
            tmp = x1 
            x1 = x2
            x2 = tmp
        if (y2 < y1):
            tmp = y1
            y1 = y2
            y2 = tmp

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                al.add(y * 1j + x)
                ABYSS = max(y + 1, ABYSS)

t = 0
i = 100000000000000
flag = 0

while i > 0:
    sand = 500
    while i > 0:
        if flag:
            break
        if (sand.imag >= ABYSS):
            print(t)
            flag = 1
        elif (sand + 1j not in al):
            sand += 1j
            continue
        elif (sand + 1j - 1 not in al):
            sand += -1 + 1j
            continue
        elif (sand + 1j + 1 not in al):
            sand += 1 + 1j
            continue
        al.add(sand)
        t += 1
        i -= 1
        break
    if flag:
        break