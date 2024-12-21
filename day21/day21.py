import sys
from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def trav(maze, x, y, completed, path):
    out = [(maze[y][x], path)]
    for dx, dy, c in ((0, 1, "v"), (1, 0, ">"), (-1, 0, "<"), (0, -1, "^")):
        cand = (x + dx, y + dy)
        if cand not in completed and 0 <= cand[0] < len(maze[0]) and 0 <= cand[1] < len(maze):
            if maze[dy + y][dx + x] != " ":
                com2 = completed.copy()
                com2.append(cand)
                path2 = path + c
                for r in trav(maze, cand[0], cand[1], com2, path2):
                    out.append(r)

    return out


def calc_moves(maze, chars):
    moves = defaultdict(list)
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            c = maze[y][x]
            if c != " ":
                all_paths = trav(maze, x, y, [(x, y)], "")
                for target in chars:
                    if target != c:
                        paths_for_target = [x for x in all_paths if x[0] == target]
                        min_len_for_target = sys.maxsize
                        for x in paths_for_target:
                            min_len_for_target = min(min_len_for_target, len(x[1]))
                        for x in paths_for_target:
                            if len(x[1]) == min_len_for_target:
                                moves[c + target].append(x[1])
    return moves


def get_sequences(seq, moves):
    outs = [""]
    last = "A"
    for c in seq:
        if last != c:
            cands = moves[last + c]
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
        candidates = get_sequences(l, moves_numerical)
        compl = sys.maxsize
        for c in candidates:
            my_compl = f(c, n)
            compl = min(my_compl, compl)
        out += num * compl
    return out


num_pad = [list("789"), list("456"), list("123"), list(" 0A")]
dir_pad = [list(" ^A"), list("<v>")]

moves_numerical = calc_moves(num_pad, "A0123456789")
moves_directional = calc_moves(dir_pad, "A^<v>")

p1 = solve(2)
p2 = solve(25)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
