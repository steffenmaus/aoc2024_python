import re
from collections import defaultdict

with open('input.txt') as file:
    ints = [[int(n) for n in re.findall(r'-?\d+', line)] for line in file]


def find_tree(robots):
    for time in range(X * Y):
        maze = set()
        for i, _ in enumerate(robots):
            px, py, vx, vy = robots[i]
            newx = (px + vx) % X
            newy = (py + vy) % Y
            robots[i] = (newx, newy, vx, vy)
            maze.add((newx, newy))

        for y in range(Y):
            li = ""
            for x in range(X):
                p = (x, y)
                if p in maze:
                    li = li + "#"
                else:
                    li = li + " "
            if "###############################" in li:
                return time + 1
    return 0


Y = 103
X = 101

seed = []
for l in ints:
    px, py, vx, vy = l
    seed.append((px, py, vx, vy))

robots = seed.copy()
for _ in range(100):
    for i, _ in enumerate(robots):
        px, py, vx, vy = robots[i]
        newx = (px + vx) % X
        newy = (py + vy) % Y
        robots[i] = (newx, newy, vx, vy)

count = defaultdict(int)
for px, py, vx, vy in robots:
    count[(px, py)] += 1

q1, q2, q3, q4 = 0, 0, 0, 0
for y in range(Y):
    for x in range(X):
        if x < X // 2 and y < Y // 2:
            q1 += count[(x, y)]
        if x > X // 2 and y > Y // 2:
            q2 += count[(x, y)]
        if x > X // 2 and y < Y // 2:
            q3 += count[(x, y)]
        if x < X // 2 and y > Y // 2:
            q4 += count[(x, y)]

p1 = q1 * q2 * q3 * q4
print("Part 1: " + str(p1))

p2 = find_tree(seed.copy())
print("Part 2: " + str(p2))
