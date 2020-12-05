from math import floor, ceil
f = open("input", "r")

ls = []

for l in f:
    ls.append(l.rstrip())

def part(num1, num2, upper):
    if upper:
        return num1 + ceil((num2-num1)/2), num2
    else:
        return num1, num1 + floor((num2-num1)/2)

def init():
    seats = []
    for i in range(128):
        row = []
        for j in range(8):
            row.append(False)
        seats.append(row)

    return seats

def calc(seq):
    row = 0, 127
    col = 0, 7
    seq = (seq[0:7], seq[7:10])
    for c in seq[0]:
        if c == 'F':
            row = part(row[0], row[1], False)
        else:
            row = part(row[0], row[1], True)
    for c in seq[1]:
        if c == 'L':
            col = part(col[0], col[1], False)
        else:
            col = part(col[0], col[1], True)

    return row[0], col[0], row[0]*8+col[0]

#   BFFFBBFRRR: row 70, column 7, seat ID 567.
#   FFFBBBFRRR: row 14, column 7, seat ID 119.
#   BBFFBBFRLL: row 102, column 4, seat ID 820.

m = 0
seats = init()

for l in ls:
    r,c, n = calc(l)
    m = max(m, n)
    seats[r][c] = True

print(m)
for i in range(127):
    for j in range(8):
        if not seats[i][j]:
            print((i,j))

