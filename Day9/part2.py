#!/usr/bin/env python3
f = open("in.txt").read().strip().split("\n")

lst = [(0, 0) for x in range(10)]
directions = {"L": -1, "R": 1, "U": 1, "D": -1}
visited = set(lst)

def disctanceBetweenTwo(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

def add(a, b):
    return tuple(map(lambda i, j: i + j, a, b))

for line in f:
    a = line.split(" ")
    command, distance = a[0], int(a[1])

    for r in range(distance):

        # Add to y coordinate
        if command == "R" or command == "L":
            lst[0] = add(lst[0], (0, directions[command]))
        # Add to x coordinate
        else:
            lst[0] = add(lst[0], (directions[command], 0))

        for i in range(1, len(lst)):
            d2 = tuple(map(lambda i, j: i - j, lst[i - 1], lst[i]))

            # If the distance between them is more than 1 then move tail
            if (disctanceBetweenTwo(lst[i - 1], lst[i])) >= 2:
                ch = (int(d2[0] / 2), int(d2[1] / 2))
                lst[i] = tuple(map(lambda i, j: i - j, lst[i - 1], ch))

        visited.add(lst[-1])

print(len(visited))