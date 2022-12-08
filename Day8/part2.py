#!/usr/bin/env python3
with open("in.txt", "r") as f:
    a = [[int(znak) for znak in vrstica.rstrip("\n")] for vrstica in f]

def up(x, y, drevo, sum=0):
    for r in reversed(range(0, x)):
        sum += 1
        if drevo <= a[r][y]:
            break
    return sum

def down(x, y, drevo, sum=0):
    for r in range(x + 1, len(a[0])):
        sum += 1
        if drevo <= a[r][y]:
            break
    return sum

def left(x, y, drevo, sum=0):
    for r in reversed(range(0, y)):
        sum += 1
        if drevo <= a[x][r]:
            break
    return sum

def right(x, y, drevo, sum=0):
    for r in range(y + 1, len(a)):
        sum += 1
        if drevo <= a[x][r]:
            break
    return sum


bestTreeScore = 0

for x in range(0, len(a)):
    for y in range(0, len(a[0])):
        drevo = a[x][y]
        treeScore = left(x, y, drevo) * right(x, y, drevo) * up(x, y, drevo) * down(x, y, drevo)
        bestTreeScore = max(treeScore, bestTreeScore)

print(bestTreeScore)
