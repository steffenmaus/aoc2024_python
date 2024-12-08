import math
from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

X = len(lines[0])
Y = len(lines)

ant = defaultdict(list)
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        if c != ".":
            ant[c].append(p)


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
                    if manh_d(p, q) == 2 * manh_d(p, q2) or not p1:
                        return True
    return False


antinodes1 = set()
antinodes2 = set()
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        for target in ant.keys():
            if f(p, ant[target], True):
                antinodes1.add(p)
            if f(p, ant[target], False):
                antinodes2.add(p)
            elif p in ant[target] and len(ant[target]) > 1:
                antinodes2.add(p)

p1 = len(antinodes1)
p2 = len(antinodes2)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
