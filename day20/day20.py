with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_all_nei_2d_4(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r

def get_all_nei_within_man_dist(p, max_dist):
    x, y = p
    out = set()
    for d in range(1, max_dist + 1):
        for dx in range(d+1):
            dy = d - dx
            out.add((x + dx, y + dy))
            out.add((x + dx, y - dy))
            out.add((x - dx, y + dy))
            out.add((x - dx, y - dy))
    return out

def steps_in_maze(start):
    out = {}
    border = set()
    border.add(start)
    completed = set()
    steps = 0
    while border:
        next_border = set()
        completed.update(border)
        for p in border:
            out[p] = steps
            for n in get_all_nei_2d_4(p):
                if n in floor and n not in completed:
                    next_border.add(n)
        border = next_border
        steps += 1
    return out


def f(cheat_time):
    out = 0
    for p in floor:
        for p2 in get_all_nei_within_man_dist(p, cheat_time):
            if p != p2 and p2 in floor:
                if distances_from_start[p] + distances_to_end[p2] + man_dist(p, p2) <= best_distance - 100:
                    out += 1
    return out


X = len(lines[0])
Y = len(lines)

floor = set()
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        match lines[y][x]:
            case ".":
                floor.add(p)
            case "E":
                target = p
                floor.add(p)
            case "S":
                start = p
                floor.add(p)



distances_from_start = steps_in_maze(start)
distances_to_end = steps_in_maze(target)
best_distance = distances_from_start[target]

p1 = f(2)
p2 = f(20)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
