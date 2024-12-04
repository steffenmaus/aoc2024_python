with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

grid = {}


def find(p, dx, dy, open):
    if not open:
        return True
    else:
        if grid.get(p, "") == open[0]:
            return find((p[0] + dx, p[1] + dy), dx, dy, open[1:])
        else:
            return False


def matches(p):
    c = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx != 0 or dy != 0:
                c += find(p, dx, dy, "XMAS")
    return c


def matches_2(p):
    x, y = p
    return ((find((x - 1, y - 1), 1, 1, "MAS") or find((x - 1, y - 1), 1, 1, "SAM")) and
            (find((x - 1, y + 1), 1, -1, "MAS") or find((x - 1, y + 1), 1, -1, "SAM")))


X = len(lines[0])
Y = len(lines)

p1 = 0
p2 = 0

for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        grid[p] = c

for y in range(0, Y):
    for x in range(0, X):
        p1 += matches((x, y))
        p2 += matches_2((x, y))

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
