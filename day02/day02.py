with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_deltas(ints):
    deltas = []
    prev = ints[0]
    for i in range(1, len(ints)):
        deltas.append(ints[i] - prev)
        prev = ints[i]
    return deltas


def f(ints):
    deltas = get_deltas(ints)
    return all([x in (1, 2, 3) for x in deltas]) or all([x in (-1, -2, -3) for x in deltas])


p1 = 0
p2 = 0

for l in lines:
    ints = list(map(int, l.split()))

    p1 += f(ints)
    maybe = False
    for i in range(len(ints)):
        temp = ints.copy()
        temp.pop(i)
        if f(temp):
            maybe = True
    if maybe:
        p2 += 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
