from sys import stdin
import heapq
T = int(stdin.readline())

while T > 0:
    T -= 1

    N, K = map(int, stdin.readline().split(' '))
    rules = {}
    D = list(map(int, stdin.readline().split(' ')))
    for _ in range(K):
        x, y = map(int, stdin.readline().split(' '))
        try:
            rules[y].append(x)
        except KeyError:
            rules[y] = [x]
    W = int(stdin.readline())

    cands = rules[W]
    for cand in cands:
        D[cand-1] += D[W-1]




