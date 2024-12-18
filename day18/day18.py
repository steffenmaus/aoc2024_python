with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei_2d_4(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


def f(maze, start, target):
    border = set()
    border.add(start)
    completed = set()
    steps = 0
    while border:
        if target in border:
            return steps
        next_border = set()
        completed.update(border)
        for p in border:
            for n in get_all_nei_2d_4(p):
                if n in maze.keys() and n not in completed:
                    if maze[n] == ".":
                        next_border.add(n)
        border = next_border
        steps += 1
    return None


X = 71
Y = 71
maze = {}

for y in range(Y):
    for x in range(X):
        maze[(x, y)] = "."

start = (0, 0)
target = (70, 70)

for l in lines[:1024]:
    x, y = list(map(int, l.split(",")))
    maze[(x, y)] = "#"

p1 = f(maze, start, target)
print("Part 1: " + str(p1))

for l in lines[1023:]:
    x, y = list(map(int, l.split(",")))
    maze[(x, y)] = "#"
    if f(maze, start, target) is None:
        p2 = str(x) + "," + str(y)
        break

print("Part 2: " + str(p2))
