from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_deltas(ints):
    deltas = []
    prev = ints[0]
    for i in range(1, len(ints)):
        deltas.append(ints[i] - prev)
        prev = ints[i]
    return deltas


endings = []

p1 = 0

for l in lines:
    ends = []
    current = int(l)
    for i in range(2000):
        ends.append(current % 10)
        current = ((current * 64) ^ current) % 16777216
        current = ((current // 32) ^ current) % 16777216
        current = ((current * 2048) ^ current) % 16777216
    ends.append(current % 10)
    endings.append(ends)
    p1 += current

print("Part 1: " + str(p1))

bananas_per_pattern = defaultdict(int)
for ends in endings:
    my_patterns = set()
    delt = get_deltas(ends)
    pos = 0
    while pos < len(ends) - 4:
        pattern = ",".join(str(x) for x in delt[pos:pos + 4])
        if pattern not in my_patterns:
            bananas_per_pattern[pattern] += ends[pos + 4]
            my_patterns.add(pattern)
        pos += 1

p2 = 0
for pot in bananas_per_pattern:
    p2 = max(p2, bananas_per_pattern[pot])

print("Part 2: " + str(p2))
