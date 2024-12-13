import re

from z3 import *

with open('input.txt') as file:
    ints = [[int(n) for n in re.findall(r'-?\d+', line)] for line in file]


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


groups = get_groups_from_lines(ints)

print("Linear algebra approach:")


def calc(target, a, b):
    px, py = target
    ax, ay = a
    bx, by = b

    bcount = (py * ax - px * ay) / (by * ax - bx * ay)
    acount = (px - bcount * bx) / ax

    if acount % 1 == 0 and bcount % 1 == 0:
        return 3 * int(acount) + int(bcount)
    else:
        return 0


p1 = 0
p2 = 0
for g in groups:
    a, b, p = g
    ax, ay = a
    bx, by = b
    px, py = p
    p1 += calc((px, py), (ax, ay), (bx, by))
    p2 += calc((px + 10000000000000, py + 10000000000000), (ax, ay), (bx, by))

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
print("---")

print("Solver approach:")


def solve(target, a, b):
    my_solver = z3.Solver()
    px, py = target
    ax, ay = a
    bx, by = b

    acount = Int('acount')
    bcount = Int('bcount')
    my_solver.add(px == ax * acount + bx * bcount)
    my_solver.add(py == ay * acount + by * bcount)
    if my_solver.check() == z3.sat:
        model = my_solver.model()
        return model.eval(acount).as_long() * 3 + model.eval(bcount).as_long()
    else:
        return 0


p1 = 0
p2 = 0
for g in groups:
    a, b, p = g
    ax, ay = a
    bx, by = b
    px, py = p
    p1 += solve((px, py), (ax, ay), (bx, by))
    p2 += solve((px + 10000000000000, py + 10000000000000), (ax, ay), (bx, by))

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
print("---")

print("DP approach (will fail on part 2):")

mem = {}


def dp(target, current, a, b, cost):
    px, py = target
    cx, cy = current
    ax, ay = a
    bx, by = b

    if (px - cx, py - cy, a, b) in mem.keys():
        return mem[(px - cx, py - cy, a, b)]
    if current == target:
        return cost
    if current[0] > target[0] or current[1] > target[1]:
        return sys.maxsize

    na = dp(target, (cx + ax, cy + ay), a, b, cost + 3)
    nb = dp(target, (cx + bx, cy + by), a, b, cost + 1)

    mem[(px - cx, py - cy, a, b)] = min(na, nb)
    return min(na, nb)


p1 = 0
for g in groups:
    a, b, p = g
    ax, ay = a
    bx, by = b
    px, py = p
    res = dp((px, py), (0, 0), (ax, ay), (bx, by), 0)
    if res < sys.maxsize:
        p1 += res
print("Part 1: " + str(p1))

