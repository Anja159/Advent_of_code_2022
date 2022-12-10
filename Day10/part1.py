#!/usr/bin/env python3
f = open("in.txt", "r")
X = 1
cycle = 0
cycles = [20, 60, 100, 140, 180, 220]
signalStrenght = 0

for vrstica in f:

    if vrstica.strip() == "noop":
        cycle += 1
        if cycle in cycles:
            signalStrenght += cycle * X
    else:
        a = vrstica.strip().split(" ")
        for _ in range(0, 2):
            cycle += 1
            if cycle in cycles:
                signalStrenght += cycle * X
        X += int(a[1])

print(signalStrenght)
