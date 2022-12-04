#!/usr/bin/python
f = open("in.txt", "r")
overlapping = 0

for vrstica in f:
    a = vrstica.split(",")
    prvi, drugi = a[0].split("-"), a[1].split("-")

    if (int(prvi[0]) >= int(drugi[0]) and int(prvi[1]) <= int(drugi[1])) or (
        int(prvi[0]) <= int(drugi[0]) and int(prvi[1]) >= int(drugi[1])):
        overlapping += 1

print(overlapping)