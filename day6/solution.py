from math import floor, ceil
f = open("input", "r")

groups = []
group = set()

for l in f:
    if l.rstrip() == "":
        groups.append(group)
        print(group)
        group = set()
    else:
        for c in l.rstrip():
            group.add(c)


cnt = 0
for g in groups:
    cnt += len(g)

print(cnt)
