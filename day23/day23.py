from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_network_id(comps):
    return ",".join(sorted(comps))


mem_f = {}


def f(completed, candidates, target_size):
    completed_id = get_network_id(completed)
    if completed_id in mem_f.keys():
        return mem_f[completed_id]
    out = set()
    if len(completed) == target_size:
        return {get_network_id(completed)}
    if not candidates:
        return {}
    for c in candidates:
        for r in f(completed.union({c}), candidates.intersection(connections[c]), target_size):
            out.add(r)
    mem_f[completed_id] = out
    return out


mem_g = {}


def g(completed, candidates):
    completed_id = get_network_id(completed)
    if completed_id in mem_g.keys():
        return mem_g[completed_id]
    out = set()
    if not candidates:
        return {get_network_id(completed)}
    for c in candidates:
        for r in g(completed.union({c}), candidates.intersection(connections[c])):
            out.add(r)
    mem_g[completed_id] = out
    return out


connections = defaultdict(list)

for l in lines:
    a, b = l.split("-")
    connections[a].append(b)
    connections[b].append(a)

lans = set()
for c in connections.keys():
    if c.startswith("t"):
        for r in f({c}, set(connections[c]), 3):
            lans.add(r)
p1 = len(lans)

print("Part 1: " + str(p1))

bestSize = 0
p2 = None
for c in connections.keys():
    for r in g({c}, set(connections[c])):
        if len(r) > bestSize:
            bestSize = len(r)
            p2 = r

print("Part 2: " + str(p2))
