from math import floor, ceil
f = open("input", "r")

bag_rules = {}

for l in f:
    l = l.rstrip()
    ls = l.split(" bags contain ")
    color = ls[0]
    bag_rules[color] = []
    ls = ls[1].split(",")
    for b in ls:
        if "no other bags." not in b:
            bag_rules[color].append(b[2:].replace("bags", "").replace("bag", "").replace(".", "").strip(" "))



goal = "shiny gold"
cnt = 0

def contain_goal(bag):
    for c in bag:
        if c == "shiny gold":
            print(f"{c}", end="")
            return True

        if c in bag_rules and contain_goal(bag_rules[c]):
            print(f", {c}", end="")
            return True

    return False

for bag in bag_rules:
    if contain_goal(bag_rules[bag]):
        print()
        cnt += 1

contain_goal(bag_rules["shiny teal"])

print(cnt)
#{"bag color" : [{"color", "cnt"}, {"color", "cnt"}]}


