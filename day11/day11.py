with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def f(x, times):
    if (x, times) in mem:
        return mem[(x, times)]
    else:
        res = []
        if x == 0:
            res.append(1)
        elif len(str(x)) % 2 == 0:
            s = str(x)
            l = len(s) // 2
            res.append(int(s[:l]))
            res.append(int(s[l:]))
        else:
            res.append(2024 * x)
        if times == 1:
            mem[(x, times)] = len(res)
            return len(res)
        else:
            ret = 0
            for temp in res:
                ret += f(temp, times - 1)
        mem[(x, times)] = ret
        return ret


p1 = 0
p2 = 0

seed = list(map(int, lines[0].split()))

mem = {}

for s in seed:
    p1 += f(s, 25)
    p2 += f(s, 75)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
