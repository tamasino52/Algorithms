from sys import stdin
import sys
sys.setrecursionlimit(10**6)

N = int(stdin.readline())
nodes = list(stdin.readline())[:-1]

adj = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, stdin.readline().split(' '))
    u, v = u-1, v-1
    adj[u].append(v)
    adj[v].append(u)


def fn(root, curr, word):
    words = [word]
    max_v = '0'
    for i in adj[curr]:
        if i != root:
            max_v = max(max_v, nodes[i])
    for i in adj[curr]:
        if i != root and max_v == nodes[i]:
            words += (fn(curr, i, word + nodes[i]))
    return words


print(max(fn(0, 0, nodes[0])))
