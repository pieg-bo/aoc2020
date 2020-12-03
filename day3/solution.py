f = open("input", "r")



ls = []

for l in f:
    ls.append([c == "#" for c in l.rstrip()])


w = len(ls[0])

def next_pos(x, y, dx, dy):
    x = (x + dx) % w
    y += dy
    return x, y

def calc_slope(dx, dy):
    cnt = 0
    x = 0
    y = 0
    while y < len(ls):
        if ls[y][x]:
            cnt += 1

        x, y = next_pos(x, y, dx, dy)
    return cnt



print(calc_slope(3, 1))

print(calc_slope(1, 1)*
      calc_slope(3, 1)*
      calc_slope( 5, 1)*
      calc_slope( 7, 1)*
      calc_slope( 1, 2))
