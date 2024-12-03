with open('input.txt') as file:
    line = file.read()

p1 = 0
p2 = 0

do = True
for i in range(len(line)):
    current = line[i:]

    if current.startswith("mul(") and 0 < current.find(",") < current.find(")"):
        args = current.split("mul(")[1].split(")")[0].split(",")
        if len(args) == 2:
            a, b = args
            if len(a) in (1, 2, 3) and len(b) in (1, 2, 3):
                if a.isnumeric() and b.isnumeric():
                    p1 += int(a) * int(b)
                    if do:
                        p2 += int(a) * int(b)

    elif current.startswith("do()"):
        do = True
    elif current.startswith("don't()"):
        do = False

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
