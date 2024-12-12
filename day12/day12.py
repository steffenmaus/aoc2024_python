with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei_2d_4(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


def flood_maze(maze, start):
    k = maze[start]
    open = set()
    completed = set()
    open.add(start)
    while open:
        current = open.pop()
        completed.add(current)
        for n in get_all_nei_2d_4(current):
            if n in maze.keys() and n not in completed:
                if maze[n] == k:
                    open.add(n)
    return completed


def next_in_dir(p, dir):
    x, y = p
    match dir % 4:
        case 0:
            return x, y - 1
        case 1:
            return x + 1, y
        case 2:
            return x, y + 1
        case 3:
            return x - 1, y


def right_in_dir(p, dir):
    x, y = p
    match dir % 4:
        case 0:
            return (x + 1, y)
        case 1:
            return (x, y + 1)
        case 2:
            return (x - 1, y)
        case 3:
            return (x, y - 1)


X = len(lines[0])
Y = len(lines)

p1 = 0
p2 = 0

maze = {}
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        maze[p] = c

comp = set()
total = []

for y in range(Y):
    for x in range(X):
        p = (x, y)
        if p not in comp:
            res = flood_maze(maze, p)
            total.append(res)
            for l in res:
                comp.add(l)


def traverse_a_point(area, start):
    sides = 0
    current = start
    dir = 0
    visited = set()
    visited.add(start)
    mem = {}
    while True:
        if (current, dir % 4) in mem.keys():  # this catches a bug I have not found yet...
            return sides - mem[(current, dir % 4)], visited
        mem[(current, dir % 4)] = sides
        if current == start and dir % 4 == 0 and sides > 1:
            return sides, visited
        cand = next_in_dir(current, dir)
        if cand not in area and right_in_dir(cand, dir) in area:
            current = cand
            visited.add(current)
        elif cand in area:
            sides += 1
            dir -= 1
        else:
            sides += 1
            dir += 1
            current = cand
            current = next_in_dir(current, dir)
            visited.add(current)


def sides(area):
    cands = set()
    for e in area:
        x, y = e
        if (x - 1, y) not in area:
            cands.add((x - 1, y))

    sides = 0
    while cands:
        curr = cands.pop()
        ret = traverse_a_point(area, curr)
        sides += ret[0]
        for x in ret[1]:
            cands.discard(x)
    return sides


for area in total:
    size = len(area)
    peri = 0
    for p in area:
        for n in get_all_nei_2d_4(p):
            if n in maze.keys() and maze[n] != maze[p] or n not in maze.keys():
                peri += 1
    p1 += size * peri
    p2 += size * sides(area)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
