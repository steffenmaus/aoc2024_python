with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

p1 = 0
p2 = 0

ls = []
rs = []

for l in lines:
    ls.append(int(l.split()[0]))
    rs.append(int(l.split()[1]))

ls.sort()
rs.sort()
for i, _ in enumerate(ls):
    d = abs(ls[i] - rs[i])
    p1 += d

for x in ls:
    c = 0
    for y in rs:
        if x == y:
            c += 1
    p2 += x * c


print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
