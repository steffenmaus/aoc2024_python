with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def checksum(disk):
    sum = 0
    for i, v in enumerate(disk):
        if v is not None:
            sum += i * v
    return sum


def f1(disk):
    space = []
    for i, v in enumerate(disk):
        if v is None:
            space.append(i)

    for i in reversed(range(len(disk))):
        v = disk[i]
        if v is not None:
            target = space.pop(0)
            if target >= i:
                break
            disk[target] = v
            disk[i] = None

    return checksum(disk)


def f2(disk, positions):
    for id in sorted(positions.keys(), reverse=True):
        x, y = positions[id]
        size = y - x
        s = 0
        for i, v in enumerate(disk):
            if i >= x:
                break
            if v is None:
                s += 1
                if s == size:
                    for old in range(x, y):
                        disk[old] = None
                    for x in range(s):
                        disk[i - x] = id
                    break
            else:
                s = 0

    return checksum(disk)


initial = list(map(int, lines[0]))
disk = []
id = 0
positions = {}
pos = 0
file = True
for c in initial:
    if file:
        positions[id] = (pos, pos + c)
        pos += c
        disk += [id] * c
        id += 1
    else:
        pos += c
        disk += [None] * c
    file = not file

p1 = f1(disk.copy())
print("Part 1: " + str(p1))

p2 = f2(disk.copy(), positions)
print("Part 2: " + str(p2))
