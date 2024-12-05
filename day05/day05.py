from collections import defaultdict

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


def get_middle_entry(list):
    return list[len(list) // 2]


def find_valid_order_with_preconds(elements, preconds):
    out = []
    while len(out) != len(elements):
        for e in elements:
            if e not in out:
                if all(x in out or x not in elements for x in preconds[e]):
                    out.append(e)
                    break
    return out


groups = get_groups_from_lines(lines)

p1 = 0
p2 = 0

rules, updates = groups

preconds = defaultdict(list)

for u in rules:
    a, b = u.split("|")
    preconds[b].append(a)

for u in updates:
    split = u.split(",")
    if split == find_valid_order_with_preconds(split, preconds):
        p1 += int(get_middle_entry(split))
    else:
        p2 += int(get_middle_entry(find_valid_order_with_preconds(split, preconds)))

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
