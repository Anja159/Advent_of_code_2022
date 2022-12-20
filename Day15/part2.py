import re
from z3 import If, Int, Solver

f = open("in.txt", "r")
h = []
s = Solver()

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


# My first time using z3
def abs(x):
    return If(x >= 0, x, -x)


x, y = Int("x"), Int("y")
s.add(x >= 0)
s.add(x <= 4000000)
s.add(y >= 0)
s.add(y <= 4000000)

for n in h:
    a, b = (n[0], n[1]), (n[2], n[3])
    dist = manhattan(a, b)
    s.add(abs(x - n[0]) + abs(y - n[1]) > dist)

s.check()
model = s.model()
model1 = model[x].as_long() * 4000000
model2 = model[y].as_long()
print(model1 + model2)
