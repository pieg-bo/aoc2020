f = open("input", "r")

numbers = []

for l in f:
    l = l.rstrip()
    numbers.append(int(l))

def check_number(i):
    preamble = numbers[i-25:i]
    for x in range(25):
        for y in range(25):
            if x != y and preamble[x] + preamble[y] == numbers[i]:
                return True
    return False

def invalid_number():
    for i in range(25, len(numbers)):
        if not check_number(i):
            return(numbers[i])

goal = invalid_number()
print(goal)

def test_range(start_pos):
    cnt = numbers[start_pos]
    i = start_pos + 1
    while cnt < goal and i < len(numbers):
        cnt += numbers[i]
        if cnt == goal:
            r = numbers[start_pos:i+1]
            return min(r) + max(r)

        i += 1
    return -1

for i in range(len(numbers)):
    num = test_range(i)
    if num != -1:
        print(num)
        break


