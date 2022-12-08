#!/usr/bin/env python3
with open("in.txt", "r") as f:
    a = [[int(znak) for znak in vrstica.rstrip("\n")] for vrstica in f]

def up(x, y, drevo):
    for r in range(0, x):
        if drevo <= a[r][y]:
            return False
    return True

def down(x, y, drevo):
    for r in range(x + 1, len(a[0])):
        if drevo <= a[r][y]:
            return False
    return True

def left(x, y, drevo):
    for r in range(0, y):
        if drevo <= a[x][r]:
            return False
    return True


def right(x, y, drevo):
    for r in range(y + 1, len(a)):
        if drevo <= a[x][r]:
            return False
    return True


numVisible = 0

for x in range(0, len(a)):
    for y in range(0, len(a[0])):
        drevo = a[x][y]
        if (up(x, y, drevo) or down(x, y, drevo) or left(x, y, drevo) or right(x, y, drevo)):
            numVisible += 1

print(numVisible)
