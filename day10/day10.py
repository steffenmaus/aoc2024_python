with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei_2d_4(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


def valid_trails(p, height):
    if maze[p] != height:
        return []
    if height == 9:
        return [p]
    out = []
    for n in get_all_nei_2d_4(p):
        if n in maze.keys():
            for x in valid_trails(n, height + 1):
                out.append(x)
    return out


X = len(lines[0])
Y = len(lines)

p1 = 0
p2 = 0

maze = {}
for y in range(0, Y):
    for x in range(0, X):
        maze[(x, y)] = int(lines[y][x])

for y in range(0, Y):
    for x in range(0, X):
        res = valid_trails((x, y), 0)
        p1 += len(set(res))
        p2 += len(res)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
