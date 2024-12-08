with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

X = len(lines[0])
Y = len(lines)

p1 = 0
p2 = 0

ant = {}
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        if c != ".":
            if c in ant.keys():
                ant[c].append(p)
            else:
                ant[c] = list()
                ant[c].append(p)
import math


def cart_to_rad(x, y):
    if x > 0:
        return math.atan(y / x)
    elif x < 0 and y >= 0:
        return math.atan(y / x) + math.pi
    elif x < 0 and y < 0:
        return math.atan(y / x) - math.pi
    elif x == 0 and y > 0:
        return math.pi / 2
    elif x == 0 and y < 0:
        return -math.pi / 2


def manh_d(p, q):
    x, y = p
    x2, y2 = q
    return abs(x - x2) + abs(y - y2)


def f(p, points, p1):
    for q in points:
        for q2 in points:
            if q != q2:
                if cart_to_rad(p[0] - q[0], p[1] - q[1]) == cart_to_rad(p[0] - q2[0], p[1] - q2[1]):
                    d = manh_d(q, q2)
                    if p1:
                        if manh_d(p, q) == 2 * manh_d(p, q2):
                            return True
                    else:
                        if manh_d(p, q) % d == 0 and manh_d(p, q2) % d == 0:
                            return True
    return False


for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        ok = False
        ok2 = False
        for target in ant.keys():
            if f(p, ant[target], True):
                ok = True
            if f(p, ant[target], False):
                ok2 = True
            if p in ant[target] and len(ant[target]) > 1:
                ok2 = True
        p1 += ok
        p2 += ok2

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
