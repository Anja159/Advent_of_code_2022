#!/usr/bin/python
f = open("in.txt", "r")

kalorije = 0
sumkalorij = []

for vrstica in f:
    if len(vrstica) <= 1:
        sumkalorij.append(kalorije)
        kalorije = 0
    else:
        kalorije += int(vrstica)

sumkalorij.sort(reverse=True)
print(sumkalorij[0] + sumkalorij[1] + sumkalorij[2])