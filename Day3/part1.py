#!/usr/bin/python
f = open("in.txt", "r")
priority = 0

for vrstica in f:
    prviDel, drugiDel = vrstica[: len(vrstica) // 2], vrstica[len(vrstica) // 2 :]
    presek = list(set(list(prviDel)).intersection(list(drugiDel)))

    if presek[0].isupper():
        priority += ord(presek[0]) - 38
    else:
        priority += ord(presek[0]) - 96
        
print(priority)