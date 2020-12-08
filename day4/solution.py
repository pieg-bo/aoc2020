import re
f = open("input", "r")

s = ""
for l in f:
    s += l

s = s.replace(" ", "\n")

ls = []
passport = {}

for l in s.split("\n"):
    l = l.rstrip()
    if l.rstrip() == "":
        ls.append(passport)
        passport = {}
    else:
        field = l.split(":")
        if field[0] != "cid":
            passport[field[0]] = field[1]

def validate_hgt(hgt):
    if "cm" in hgt:
        return 150 <= int(hgt[:-2]) <= 193
    if "in" in hgt:
        return 59 <= int(hgt[:-2]) <= 76
    return False

eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def validate(pp):
    return (1920 <= int(pp['byr']) <= 2002 and
            2010 <= int(pp['iyr']) <= 2020 and
            2020 <= int(pp['eyr']) <= 2030 and
            2020 <= int(pp['eyr']) <= 2030 and
            validate_hgt(pp['hgt']) and
            re.match("#[0-9a-f]{6}", pp['hcl']) != None and
            len(pp['hcl']) == 7 and
            pp['ecl'] in eye_colors and
            re.match("[0-9]{9}", pp['pid']) != None and
            len(pp['pid']) == 9
            )

cnt = 0
for pp in ls:
    if len(pp) == 7 and validate(pp):
        cnt += 1


print(len(ls))
print(cnt)



