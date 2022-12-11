#!/usr/bin/env python3
import re

f = open("in.txt").read().split("\n\n")

class Monkey:
    def __init__(self, s):

        # Parsing input
        lines = s.split("\n")
        self.items = list(map(int, re.findall("\d+", lines[1])))
        a = lines[2].split(" ")
        if a[5] == "old" and a[7] == "old":
            self.op = (lambda x: x * x) if a[6] == "*" else (lambda x: x + x)
        else:
            self.op = (
                (lambda x: x * int(a[7])) if a[6] == "*" else (lambda x: x + int(a[7]))
            )
        self.test = int(lines[3].split(" ")[5])
        self.true = int(lines[4].split(" ")[9])
        self.false = int(lines[5].split(" ")[9])
        self.inspections = 0

    def turn(self, monkeys, LCM):
        for item in self.items:
            item = self.op(item)
            
            if LCM:
                item = item % LCM
            else:
                item = item // 3
            if item % self.test:
                monkeys[self.false].items.append(item)
            else:
                monkeys[self.true].items.append(item)
            self.inspections += 1
        self.items = []


def simulation(monkeys, rounds, LCM):
    for i in range(0, rounds):
        for monkey in monkeys:
            monkey.turn(monkeys, LCM)


monkeys = [Monkey(chunk) for chunk in f]
simulation(monkeys, 20, 0)

a = []
for m in monkeys:
    a.append(m.inspections)
x = sorted(a, reverse=True)
print(x[0] * x[1])
