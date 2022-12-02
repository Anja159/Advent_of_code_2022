#!/usr/bin/python
f = open('in.txt', 'r')
sum = 0

for vrstica in f:
    a = vrstica.split(' ')
    if (a[1])[:1] == 'X':
        if a[0] == 'A':
            sum += 3
        if a[0] == 'B':
            sum += 1
        if a[0] == 'C':
            sum += 2
    if (a[1])[:1] == 'Y':
        sum += 3
        if a[0] == 'A':
            sum += 1
        if a[0] == 'B':
            sum += 2
        if a[0] == 'C':
            sum += 3
    if (a[1])[:1] == 'Z':
        sum += 6
        if a[0] == 'A':
            sum += 2
        if a[0] == 'B':
            sum += 3
        if a[0] == 'C':
            sum += 1

print (sum)