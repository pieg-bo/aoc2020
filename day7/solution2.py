#f = open("input", "r")
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
            for i in range(int(b[:2])):
                bag_rules[color].append(b[2:].replace("bags", "").replace("bag", "").replace(".", "").strip(" "))


# cnt for a level: the number of bags in that level * the sum of the children

def count_bags(bags):
    ls = []

    for bag in bags:
        ls.append(bag)
        if bag in bag_rules.keys():
            ls.extend(count_bags(bag_rules[bag]))

    return ls


print(len(count_bags(bag_rules['shiny gold'])))



