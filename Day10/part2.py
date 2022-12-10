#!/usr/bin/env python3
f = open("in.txt", "r")
X = 1
cycle = 0
cycles = [20, 60, 100, 140, 180, 220]
signalStrenght = 0

grid = [[" "] * 40 for i in range(6)]
line = 0

for vrstica in f:

    if vrstica.strip() == "noop":
        if abs(X - cycle % 40) <= 1:
            grid[line][cycle % 40] = "█"
        cycle += 1
        if cycle % 40 == 0:
            line += 1

    else:
        a = vrstica.strip().split(" ")
        for _ in range(0, 2):
            if abs(X - cycle % 40) <= 1:
                grid[line][cycle % 40] = "█"
            cycle += 1
            if cycle % 40 == 0:
                line += 1
        X += int(a[1])

for line in grid:
    print("".join(line))

"""
███  ███  ████  ██  ███   ██  ████  ██  
█  █ █  █    █ █  █ █  █ █  █    █ █  █ 
█  █ ███    █  █    █  █ █  █   █  █  █
███  █  █  █   █ ██ ███  ████  █   ████
█    █  █ █    █  █ █ █  █  █ █    █  █
█    ███  ████  ███ █  █ █  █ ████ █  █
"""