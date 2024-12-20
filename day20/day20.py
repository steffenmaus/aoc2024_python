import heapq
from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def dijkstra(start, distances):
    out = {}
    out[start] = 0
    Q = []
    for nei in distances[start]:
        node, dist = nei
        heapq.heappush(Q, (dist, node, start))
    while len(out.keys()) != len(distances.keys()):
        dist, current, prev = heapq.heappop(Q)
        if current not in out.keys():
            out[current] = dist
            for nei in distances[current]:
                n, d = nei
                heapq.heappush(Q, (d + dist, n, current))
    return out


def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_all_nei_2d_4(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


def f(cheat_time):
    out = 0
    for p in floor:
        for p2 in floor:
            if p != p2 and man_dist(p, p2) <= cheat_time:
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

distances = defaultdict(list)
for p in floor:
    for n in get_all_nei_2d_4(p):
        distances[p].append((n, 1))

distances_from_start = dijkstra(start, distances)
distances_to_end = dijkstra(target, distances)
best_distance = distances_from_start[target]

p1 = f(2)
print("Part 1: " + str(p1))

p2 = f(20)
print("Part 2: " + str(p2))
