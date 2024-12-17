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
5,5 output b%8
3,0 reset if a != 0
'''

def g(a):
    out = []
    while a != 0:
        b = a%8
        b = b^5
        c = a // 2**b
        a = a // 8
        b = b ^ c
        b = b ^ 6
        out.append(b%8)
    return out


a = ints[0][0]
prog = ints[-1]

p1 = ",".join([str(x) for x in g(a)])
print("Part 1: " + str(p1))

p2 = None

a = 0
solved = 0
temp = 0
while p2 is None:
    ta = a * 8 ** solved + temp
    res = g(ta)
    if res == prog:
        p2 = ta
    elif res[:solved + 4] == prog[:solved + 4]:
        solved += 1
        temp = ta % (8 ** solved)
        a = 0
    else:
        a += 1

print("Part 2: " + str(p2))



#not required anymore, replaced by g()
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
