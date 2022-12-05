#!/usr/bin/python
f = open("in.txt", "r")

stack1 = []
for i in range(10):
    stack1.append([])

for vrstica in f:
    # Moving crates
    if vrstica[0] == "m":
        a = vrstica.split(" ")
        for r in range(0, int(a[1])):
            element = stack1[int(a[3])].pop()
            stack1[int(a[5])].append(element)

    else:
    # Putting crates onto the stack
        parts = [vrstica[i : i + 4] for i in range(0, len(vrstica), 4)]
        st = 0

        if vrstica.find("[") == -1:
            continue

        for part in parts:
            crka = part[1:2]
            st += 1
            if crka == " ":
                continue
            stack1[st].insert(0, crka)

# Reading top elements
for h in range(0, 10):
    if len(stack1[h]):
        print(stack1[h].pop(), end="")