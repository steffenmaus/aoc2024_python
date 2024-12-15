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

lines, commands = groups
commands = "".join(commands)

X = len(lines[0])
Y = len(lines)

start = None

boxes = set()
maze = {}
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        maze[p] = c
        match c:
            case "@":
                maze[p] = "."
                start = p
            case "O":
                maze[p] = "."
                boxes.add(p)

maze2 = {}
boxes2 = {}
for y in range(Y):
    for x in range(X * 2):
        p = (x // 2, y)
        pn = (x, y)
        if p in boxes:
            if x % 2 == 0:
                boxes2[pn] = "["
            else:
                boxes2[pn] = "]"
        maze2[pn] = maze[p]


def shift_box(x, y, dx, dy):
    nx, ny = x + dx, y + dy
    if maze[(nx, ny)] == "#":
        return False
    if (nx, ny) in boxes and not shift_box(nx, ny, dx, dy):
        return False

    boxes.add((nx, ny))
    boxes.remove((x, y))
    return True


def shift_box_hor(x, y, dx):
    nx, ny = x + dx, y
    if maze2[(nx, ny)] == "#":
        return False
    if (nx, ny) in boxes2.keys() and not shift_box_hor(nx, ny, dx):
        return False

    boxes2[(nx, ny)] = boxes2[(x, y)]
    del boxes2[(x, y)]
    return True


def check_shift_box_vert(x, y, dy):
    if boxes2[(x, y)] == "[":
        l = (x, y)
        r = (x + 1, y)
        nl = (x, y + dy)
        nr = (x + 1, y + dy)
    else:
        l = (x - 1, y)
        r = (x, y)
        nl = (x - 1, y + dy)
        nr = (x, y + dy)

    affected_boxes.add((l, boxes2[l]))
    affected_boxes.add((r, boxes2[r]))

    if maze2[nl] == "#" or maze2[nr] == "#":
        return False

    if nl in boxes2.keys() and not check_shift_box_vert(nl[0], nl[1], dy):
        return False

    if nr in boxes2.keys() and not check_shift_box_vert(nr[0], nr[1], dy):
        return False

    return True


x, y = start
for c in commands:
    match c:
        case "^":
            dx, dy = 0, -1
        case ">":
            dx, dy = 1, 0
        case "v":
            dx, dy = 0, 1
        case "<":
            dx, dy = -1, 0
    nx = x + dx
    ny = y + dy
    if maze[(nx, ny)] == ".":
        if (nx, ny) not in boxes or shift_box(nx, ny, dx, dy):
            x, y = nx, ny

p1 = 0
for p in boxes:
    x, y = p
    p1 += 100 * y + x

print("Part 1: " + str(p1))

x, y = start
x = x * 2
for c in commands:
    match c:
        case "^":
            dx, dy = 0, -1
        case ">":
            dx, dy = 1, 0
        case "v":
            dx, dy = 0, 1
        case "<":
            dx, dy = -1, 0
    nx = x + dx
    ny = y + dy
    if maze2[(nx, ny)] == ".":
        if (nx, ny) not in boxes2.keys():
            x, y = nx, ny
        else:
            if abs(dy) == 0:
                if shift_box_hor(nx, ny, dx):
                    x, y = nx, ny
            else:
                affected_boxes = set()
                if check_shift_box_vert(nx, ny, dy):
                    for p, v in affected_boxes:
                        del boxes2[p]
                    for p, v in affected_boxes:
                        px, py = p
                        boxes2[(px, py + dy)] = v
                    x, y = nx, ny

p2 = 0
for p in boxes2.keys():
    x, y = p
    if boxes2[p] == "[":
        p2 += 100 * y + x

print("Part 2: " + str(p2))
