f = open("input", "r")

ls = []
for l in f:
    l = l.replace(":", "").replace("-", " ").rstrip().split(" ")
    ls.append(l)

print(ls)

# Format:  ['5', '14', 'x', 'frqqxljjwsxndx']
# Index      0     1    2           3
def check_password1(l):
    occourences = l[3].count(l[2])
    return int(l[0]) <= occourences <= int(l[1])

def check_password2(l):
    occourences = l[3].count(l[2])
    c = l[2]
    s = l[3]
    i1 = int(l[0])-1
    i2 = int(l[1])-1
    return [s[i1] == c, s[i2] == c].count(True) == 1

    
print([check_password1(l) for l in ls].count(True))
print([check_password2(l) for l in ls].count(True))
