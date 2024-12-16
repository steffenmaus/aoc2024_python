import sys

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
X = len(lines[0])
Y = len(lines)

start = None
target = None

maze = {}
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        maze[p] = c
        match c:
            case "E":
                target = p
                maze[p] = "."
            case "S":
                start = (x, y, 1)
                maze[p] = "."

import heapq


def dijkstra(start, distances):
    out = {}
    out[start] = 0
    Q = []

    for nei in distances[start]:
        node, dist = nei
        heapq.heappush(Q, (dist, node, start))
    while Q:
        dist, current, prev = heapq.heappop(Q)
        if current not in out.keys():
            out[current] = dist
            for nei in distances[current]:
                n, d = nei
                heapq.heappush(Q, (d + dist, n, current))
    return out


distances = {}
for y in range(Y):
    for x in range(X):
        for d in range(4):
            if maze[(x, y)] == ".":
                nei = []
                nei.append(((x, y, (d + 1) % 4), 1000))
                nei.append(((x, y, (d - 1) % 4), 1000))
                match d:
                    case 0:
                        nei.append(((x, y - 1, d), 1))
                    case 1:
                        nei.append(((x + 1, y, d), 1))
                    case 2:
                        nei.append(((x, y + 1, d), 1))
                    case 3:
                        nei.append(((x - 1, y, d), 1))
                distances[(x, y, d)] = nei
            else:
                distances[(x, y, d)] = []

shortest_dist = dijkstra(start, distances)
p1 = sys.maxsize
for d in range(4):
    p1 = min(p1, shortest_dist[target[0], target[1], d])

print("Part 1: " + str(p1))

shortest_dist_rev = {}
for d in range(4):
    dij = dijkstra((target[0], target[1], d), distances)
    for k in dij:
        shortest_dist_rev[k] = min(dij[k], shortest_dist_rev.get(k, sys.maxsize))

seen = set()
for y in range(Y):
    for x in range(X):
        if maze[(x, y)] == ".":
            for d in range(4):
                if shortest_dist[(x, y, d)] + shortest_dist_rev[(x, y, (d + 2) % 4)] == p1:
                    seen.add((x, y))

p2 = len(seen)
print("Part 2: " + str(p2))
