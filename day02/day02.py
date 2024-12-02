with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

p1 = 0
p2 = 0


def f(ints):
    last = ints[0]
    inc = True
    dec = True
    for i in range(1, len(ints)):
        d = ints[i] - last
        if not d in (1, 2, 3):
            inc = False
        if not d in (-1, -2, -3):
            dec = False
        last = ints[i]
    return inc or dec


for l in lines:
    ints = l.split()
    ints = [int(x) for x in ints]

    p1 += f(ints)
    maybe = False
    for i in range(len(ints)):
        if f(ints[:i] + ints[i + 1:]):
            maybe = True
    if maybe:
        p2 += 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
