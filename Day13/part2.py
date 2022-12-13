#!/usr/bin/env python3
import ast

f = open("in.txt", "r").read().strip().split("\n\n")
xy = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def compare(first, second):
    if type(first) is not list and type(second) is not list:
        return 0 if first == second else (-1 if first < second else 1)

    if type(first) is int and type(second) is list:
        first = [first]

    if type(first) is list and type(second) is int:
        second = [second]

    for firstc, secondc in zip(first, second):
        r = compare(firstc, secondc)
        if r != 0:
            return r

    return -1 if len(first) < len(second) else (0 if len(first) == len(second) else 1)


seznam = []

for x in f:
    prvi = x.split("\n")[0]
    drugi = x.split("\n")[1]
    seznam.append((ast.literal_eval(prvi), ast.literal_eval(drugi)))

packets = []

for a, b in seznam:
    packets.append(a), packets.append(b)

packets.append([[2]]), packets.append([[6]])

a = len(packets)
for i in range(0, a):
    for j in range(0, a - 1):
        if compare(packets[j], packets[j + 1]) > 0:
            temp = packets[j + 1]
            packets[j + 1] = packets[j]
            packets[j] = temp

zmnozek = 1
for i in range(a):
    if packets[i] == [[2]] or packets[i] == [[6]]:
        zmnozek *= i + 1

print(zmnozek)