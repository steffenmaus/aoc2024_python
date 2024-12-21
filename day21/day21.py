import sys
from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

# Moves not complete. sufficient for my personal input and the sample data.
# add all valid shortest moves possible (e.g. from 2 to 9)
# exeption to this rule: if you have to press a button multiple times within a path, you should press it without different buttons in between. Those will not create an optimal solution for the outter roboter.
# Example: <^< from A to 1 is NOT ideal
# Note: Adding those will still provide a valid solution, but is a waste in time and code.
moves_numeric = defaultdict(list)
moves_numeric["A"].append(("0", "<"))
moves_numeric["A"].append(("1", "^<<"))
moves_numeric["A"].append(("3", "^"))
moves_numeric["A"].append(("4", "^^<<"))
moves_numeric["A"].append(("8", "<^^^"))
moves_numeric["A"].append(("8", "^^^<"))
moves_numeric["A"].append(("9", "^^^"))

moves_numeric["1"].append(("2", ">"))
moves_numeric["1"].append(("4", "^"))
moves_numeric["1"].append(("6", ">>^"))
moves_numeric["1"].append(("6", "^>>"))
moves_numeric["1"].append(("7", "^^"))

moves_numeric["2"].append(("9", "^^>"))
moves_numeric["2"].append(("9", ">^^"))

moves_numeric["3"].append(("7", "<<^^"))
moves_numeric["3"].append(("7", "^^<<"))
moves_numeric["3"].append(("A", "v"))

moves_numeric["4"].append(("0", ">vv"))
moves_numeric["4"].append(("5", ">"))

moves_numeric["5"].append(("6", ">"))

moves_numeric["6"].append(("9", "^"))
moves_numeric["6"].append(("A", "vv"))

moves_numeric["7"].append(("0", ">vvv"))
moves_numeric["7"].append(("9", ">>"))

moves_numeric["8"].append(("0", "vvv"))

moves_numeric["9"].append(("8", "<"))
moves_numeric["9"].append(("A", "vvv"))

moves_numeric["0"].append(("2", "^"))
moves_numeric["0"].append(("3", ">^"))
moves_numeric["0"].append(("3", "^>"))
moves_numeric["0"].append(("A", ">"))

# Moves are complete.
# Again: If you have to press a button multiple times within a path, you should press it without different buttons in between.
moves_directional = defaultdict(list)
moves_directional["A"].append(("^", "<"))
moves_directional["A"].append(("v", "v<"))
moves_directional["A"].append(("v", "<v"))
moves_directional["A"].append((">", "v"))
moves_directional["A"].append(("<", "v<<"))

moves_directional["^"].append(("A", ">"))
moves_directional["^"].append(("v", "v"))
moves_directional["^"].append((">", "v>"))
moves_directional["^"].append((">", ">v"))
moves_directional["^"].append(("<", "v<"))

moves_directional["v"].append(("A", ">^"))
moves_directional["v"].append(("A", "^>"))
moves_directional["v"].append(("^", "^"))
moves_directional["v"].append((">", ">"))
moves_directional["v"].append(("<", "<"))

moves_directional["<"].append(("A", ">>^"))
moves_directional["<"].append(("^", ">^"))
moves_directional["<"].append(("v", ">"))
moves_directional["<"].append((">", ">>"))

moves_directional[">"].append(("A", "^"))
moves_directional[">"].append(("^", "<^"))
moves_directional[">"].append(("^", "^<"))
moves_directional[">"].append(("v", "<"))
moves_directional[">"].append(("<", "<<"))


def get_sequences(seq, moves):
    outs = [""]
    last = "A"
    for c in seq:
        if last != c:
            cands = [x[1] for x in moves[last] if x[0] == c]
            if len(cands) == 1:
                for i, _ in enumerate(outs):
                    outs[i] = outs[i] + cands[0] + "A"
            else:
                new_outs = []
                for cand in cands:
                    for out in outs:
                        new_outs.append(out + cand + "A")

                outs = new_outs
        else:
            for i, _ in enumerate(outs):
                outs[i] = outs[i] + "A"
        last = c
    return outs


mem = {}


def f(current, rem):
    if (current, rem) not in mem.keys():
        if rem == 0:
            mem[(current, rem)] = len(current)
        else:
            out = sys.maxsize
            candidates = get_sequences(current, moves_directional)
            for cand in candidates:
                my_out = 0
                some = [x + "A" for x in cand.split("A")][:-1]
                for x in some:
                    my_out += f(x, rem - 1)
                out = min(out, my_out)
            mem[(current, rem)] = out
    return mem[(current, rem)]


def solve(n):
    out = 0
    for l in lines:
        num = int(l[:-1])
        candidates = get_sequences(l, moves_numeric)
        compl = sys.maxsize
        for c in candidates:
            my_compl = f(c, n)
            compl = min(my_compl, compl)
        out += num * compl
    return out


p1 = solve(2)
p2 = solve(25)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
