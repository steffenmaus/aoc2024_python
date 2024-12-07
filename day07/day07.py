with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def f(target, current, rem, p1):
    if current is None:
        current = rem[0]
        rem = rem[1:]

    if target == current and not rem:
        return True
    elif current > target or not rem:
        return False
    else:
        res1 = (f(target, current + rem[0], rem[1:], p1)
                or f(target, current * rem[0], rem[1:], p1))
        if p1:
            return res1
        else:
            return res1 or f(target, int(str(current) + str(rem[0])), rem[1:], p1)


p1 = 0
p2 = 0
for l in lines:
    a, b = l.split(":")
    a = int(a)
    r = list(map(int, b.split()))
    if f(a, None, r, True):
        p1 += a
        p2 += a
    elif f(a, None, r, False):
        p2 += a

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
