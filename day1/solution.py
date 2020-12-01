f = open("input", "r")

ls = []
for l in f:
    ls.append(int(l))

print(ls)
def puzzle1():
    for i in range(len(ls)):
        for j in range(len(ls)):
            if ls[i]+ls[j] == 2020 and i != j:
                print(ls[i]*ls[j])
                return

def puzzle2():
    for i in range(len(ls)):
        for j in range(len(ls)):
            for k in range(len(ls)):
                if ls[i]+ls[j]+ls[k] == 2020 and i != j and k != j and i != k:
                    print(ls[i]*ls[j]*ls[k])
                    return

puzzle1()
puzzle2()

