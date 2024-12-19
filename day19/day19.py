with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_groups_from_lines(lines):
    groups = []
    group = []
    for l in lines:
        if not l:
            groups.append(group)
            group = []
        else:
            group.append(l)
    groups.append(group)
    return groups


upper, lower = get_groups_from_lines(lines)

colors = set()

for l in upper:
    for c in l.split(", "):
        colors.add(c)

mem = {}


def f(remaining):
    if remaining in mem.keys():
        return mem[remaining]
    if remaining == "":
        return 1
    out = 0
    for c in colors:
        if remaining.startswith(c):
            out += f(remaining[len(c):])
    mem[remaining] = out
    return out


p1 = 0
p2 = 0

for l in lower:
    res = f(l)
    p1 += res > 0
    p2 += res

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
