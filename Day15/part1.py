import re

f = open("in.txt", "r")
h = []

for vrstica in f:
    v = []
    line = vrstica.split(" ")
    v.append(int(re.sub("[^0-9-]", "", line[2])))
    v.append(int(re.sub("[^0-9-]", "", line[3])))
    v.append(int(re.sub("[^0-9-]", "", line[8])))
    v.append(int(re.sub("[^0-9-]", "", line[9])))
    h.append(v)


def manhattan(a, b):
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))


beacons = set()
tans = set()

y = 2000000

for n in h:
    a, b = (n[0], n[1]), (n[2], n[3])
    sensor = a
    beacon = b

    dist = manhattan(sensor, beacon)
    length = dist - abs(sensor[1] - y)
    beacons.add(beacon)
    sp = sensor[0] - length
    zg = sensor[0] + length + 1
    tans |= set((x, y) for x in range(sp, zg))

print(len(tans - beacons))
