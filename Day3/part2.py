#!/usr/bin/python
f = open("in.txt", "r").read()
priority = 0
vrstice = f.split("\n")

for i in range(0, len(vrstice), 3):
    prvi, drugi, tretji = vrstice[i], vrstice[i + 1], vrstice[i + 2]
    presek = list(set(list(prvi)).intersection(list(drugi)).intersection(list(tretji)))

    if presek[0].isupper():
        priority += ord(presek[0]) - 38
    else:
        priority += ord(presek[0]) - 96

print(priority)