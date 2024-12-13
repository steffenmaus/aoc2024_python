from z3 import *

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


groups = get_groups_from_lines(lines)
p1 = 0
p2 = 0

mem = {}


# not needed anymore, can still solve part 1
def f(target, current, a, b, cost):
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

    na = f(target, (cx + ax, cy + ay), a, b, cost + 3)
    nb = f(target, (cx + bx, cy + by), a, b, cost + 1)

    mem[(px - cx, py - cy, a, b)] = min(na, nb)
    return min(na, nb)


def f2(target, a, b):
    my_optimizer = z3.Optimize()
    px, py = target
    ax, ay = a
    bx, by = b

    acount = Int('acount')
    bcount = Int('bcount')
    wins = Int('wins')

    win = 0
    win += If(px == ax * acount + bx * bcount, 1, 0)
    win += If(py == ay * acount + by * bcount, 1, 0)
    my_optimizer.add(wins == win)

    my_optimizer.maximize(wins)
    my_optimizer.minimize(acount * 3 + bcount)
    my_optimizer.check()
    model = my_optimizer.model()
    w = model.eval(wins).as_long()
    if w == 2:
        return model.eval(acount).as_long() * 3 + model.eval(bcount).as_long()
    else:
        return sys.maxsize


for g in groups:
    a, b, p = g
    ax = int(a.split("X+")[1].split(",")[0])
    ay = int(a.split("Y+")[1])
    bx = int(b.split("X+")[1].split(",")[0])
    by = int(b.split("Y+")[1])
    px = int(p.split("X=")[1].split(",")[0])
    py = int(p.split("Y=")[1])
    res = f((px, py), (0, 0), (ax, ay), (bx, by), 0)
    if res < sys.maxsize:
        p1 += res
    res = f2((px + 10000000000000, py + 10000000000000), (ax, ay), (bx, by))
    if res < sys.maxsize:
        p2 += res

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
