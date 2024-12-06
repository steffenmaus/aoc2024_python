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
    return p

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




current = start
dir = 0
knowns = set()
while current in maze.keys():
    cand = next_in_dir(current, dir)
    if cand not in walls:
        current = cand
        knowns.add(current)
    else:
        dir += 1

p1 = len(knowns) - 1
print("Part 1: " + str(p1))

for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        if p in knowns and p not in walls and p != start:
            mem = set()
            current = start
            dir = 0
            while current in maze.keys():
                cand = next_in_dir(current, dir)
                if cand not in walls and cand != p:
                    current = cand
                else:
                    dir += 1
                state = (current, dir % 4)
                if state in mem:
                    p2 += 1
                    break
                else:
                    mem.add(state)

print("Part 2: " + str(p2))
