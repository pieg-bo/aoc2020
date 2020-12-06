from math import floor, ceil
f = open("input", "r")

groups = []
group = []

for l in f:
    if l.rstrip() == "":
        if len(group) != 0:
            groups.append(group)
        group = []
    else:
        p = set()
        for c in l.rstrip():
            p.add(c)
        print(p)
        group.append(p)

def intersect(group):
    if len(group) == 1:
        return group[0]

    p = group[0]
    for pp in group[1:]:
        p = p.intersection(pp)

    return p

cnt = 0
for g in groups:
    cnt += len(intersect(g))

print(cnt)
