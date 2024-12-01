with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

p1 = 0
p2 = 0

A = []
B = []

for l in lines:
    A.append(int(l.split()[0]))
    B.append(int(l.split()[1]))

A.sort()
B.sort()

for i in range(len(A)):
    p1 += abs(A[i] - B[i])

for a in A:
    p2 += a * B.count(a)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
