f = open("input", "r")

program = []
indexes = []

for l in f:
    l = l.rstrip().split(" ")
    program.append((l[0], int(l[1])))




acc = 0
pc = 0
visited = []
def execute(program):
    global pc, acc
    if pc in visited:
        return False

    visited.append(pc)

    inst = program[pc]
    if inst[0] == "nop":
        pc += 1

    if inst[0] == "acc":
        pc += 1
        acc += inst[1]

    if inst[0] == "jmp":
        pc += inst[1]

    return True

def print_status(program):
    print(f"Acc: {acc}, PC: {pc}, Next inst: {program[pc]}")

def scan_program(program):
    global indexes
    p = program.copy()
    for i in range(len(p)):
        if p[i][0] == "jmp" or p[i][0] == "nop":
            indexes.append(i)

def modify_program(program, number):
    p = program.copy()
    i = indexes[number]
    if p[i][0] == "jmp":
        p[i] = ("nop", p[i][1])
    elif p[i][0] == "nop":
        p[i] = ("jmp", p[i][1])
    print(p)
    return p

def execute_all(program):
    global visited, acc, pc
    visited = []
    acc = 0
    pc = 0
    while True:
        print_status(program)
        if not execute(program):
            return False

        if pc >= len(program):
            return True

cnt = 0
scan_program(program)
while True:
    p = modify_program(program, cnt)
    if execute_all(p):
        print(f"Good {acc}")
        break

    cnt += 1



