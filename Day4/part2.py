#!/usr/bin/python
f = open("in.txt", "r")
overlaping = 0
len = 0

for vrstica in f:
    a = vrstica.split(",")
    len += 1
    prvi, drugi = a[0].split("-"), a[1].split("-")

    if int(prvi[1]) < int(drugi[0]) or int(drugi[1]) < int(prvi[0]):
        overlaping += 1

print(len - overlaping)