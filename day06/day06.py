with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def next_in_dir(p, dir):
    x, y = p
    match dir % 4:
        case 0:
            return (x, y - 1)
        case 1:
            return (x + 1, y)
        case 2:
            return (x, y + 1)
        case 3:
            return (x - 1, y)
        case _:
            return None


def escape_maze(maze, walls, start, dir):
    current = start
    mem = set()
    while current in maze.keys():
        cand = next_in_dir(current, dir)
        if cand not in walls:
            current = cand
        else:
            dir += 1
        state = (current, dir % 4)
        if state in mem:
            return False, mem
        else:
            mem.add(state)
    return True, mem


X = len(lines[0])
Y = len(lines)

p1 = 0
p2 = 0
start = None
maze = {}

walls = set()

for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        match c:
            case ".":
                maze[p] = "."
            case "#":
                maze[p] = "#"
                walls.add(p)
            case "^":
                maze[p] = "#"
                start = p

p1_knowns = set([s[0] for s in escape_maze(maze, walls, start, 0)[1]])
p1 = len(p1_knowns)

print("Part 1: " + str(p1))

for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        if p in p1_knowns and p not in walls and p != start:
            new_walls = walls.copy()
            new_walls.add(p)
            if not escape_maze(maze, new_walls, start, 0)[0]:
                p2 += 1

print("Part 2: " + str(p2))
