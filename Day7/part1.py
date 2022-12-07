#!/usr/bin/python
f = open("in.txt", "r")
from collections import defaultdict

sum = 0
dict = defaultdict(int)
path = []

for vrstica in f:
    vrstica = vrstica.strip()
    if vrstica[0] == "$":
        cmd = vrstica.split(" ")
        if cmd[1] == "cd":
            if cmd[2] == "..":
                path.pop()
            else:
                path.append(cmd[2])
        continue

    if vrstica[0].isdigit():
        for i in range(1, len(path) + 1):
            pot = "/".join(path[:i])
            dict[pot] += int(vrstica.split(" ")[0])

for value in dict.values():
    if value <= 100000:
        sum += value

print(sum)
