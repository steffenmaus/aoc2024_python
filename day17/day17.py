import re

with open('input.txt') as file:
    ints = [[int(n) for n in re.findall(r'-?\d+', line)] for line in file]

'''
2,4, bst combo -> b  b = a % 8
1,5 bxl b -> b       b = b xor 5
7,5 dvs -> c         c = a / 2^b
0,3 dvs -> a         a = a / 8
4,1 xor -> b         b = b xor c
1,6 xor -> b         b = b xor 6
5,5 output b
3,0 reset if a != 0
'''


def f(a, prog):
    b, c = 0, 0
    pointer = 0
    out = []
    while pointer < len(prog):
        op = prog[pointer]
        litop = prog[pointer + 1]
        match litop:
            case 0:
                combo = 0
            case 1:
                combo = 1
            case 2:
                combo = 2
            case 3:
                combo = 3
            case 4:
                combo = a
            case 5:
                combo = b
            case 6:
                combo = c
        match op:
            case 0:
                a = a // 2 ** combo
                pointer += 2
            case 1:
                b = b ^ litop
                pointer += 2
            case 2:
                b = combo % 8
                pointer += 2
            case 3:
                if a == 0:
                    pointer += 2
                else:
                    pointer = litop
            case 4:
                b = b ^ c
                pointer += 2
            case 5:
                out.append(combo % 8)
                pointer += 2
            case 6:
                b = a // 2 ** combo
                pointer += 2
            case 7:
                c = a // 2 ** combo
                pointer += 2
    return out


a = ints[0][0]
prog = ints[-1]

p1 = ",".join([str(x) for x in f(a, prog)])
p2 = None

a = 0
# 0o3062346312204233
while p2 is None:
    # ta = a * 8**1 + 0o3
    # ta = a * 8**4 + 0o4233
    # ta = a * 8**9 + 0o312204233
    ta = a * 8 ** 12 + 0o346312204233
    if f(ta, prog) == prog:
        p2 = ta
    a += 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
