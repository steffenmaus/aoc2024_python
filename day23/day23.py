from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_network_id(comps):
    return ",".join(sorted(comps))


mem = {}


def f(completed, candidates):
    completed_id = get_network_id(completed)
    if completed_id in mem.keys():
        return mem[completed_id]
    out = set()
    if not candidates:
        return {get_network_id(completed)}

    for c in candidates:
        for r in f(completed.union({c}), candidates.intersection(connections[c])):
            out.add(r)
    mem[completed_id] = out
    return out


connections = defaultdict(list)

for l in lines:
    a, b = l.split("-")
    connections[a].append(b)
    connections[b].append(a)

lans = set()
for c in connections.keys():
    if c.startswith("t"):
        for n in connections[c]:
            for m in connections[c]:
                if m in connections[n]:
                    lans.add(get_network_id([c, n, m]))

p1 = len(lans)

print("Part 1: " + str(p1))

bestSize = 0
p2 = None
for c in connections.keys():
    for r in f({c}, set(connections[c])):
        if len(r) > bestSize:
            bestSize = len(r)
            p2 = r

print("Part 2: " + str(p2))
