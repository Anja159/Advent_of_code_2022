#!/usr/bin/python
f = open('in.txt', 'r')

kalorije = 0
najvecKalorij = 0

for vrstica in f:
    if len(vrstica) <= 1:
        kalorije = 0
    else:
        kalorije += int(vrstica)
        if kalorije > najvecKalorij:
            najvecKalorij = kalorije

print (najvecKalorij)