from sys import stdin
import sys

N = int(stdin.readline())
C = list(map(int, stdin.readline().split(' ')))

M = int(stdin.readline())
B = list(map(int, stdin.readline().split(' ')))

C.sort(reverse=True)
B.sort(reverse=True)

if max(B) > max(C):  # n
    print(-1)
    sys.exit()

count = 0
while len(B) > 0:  # n
    for c in range(len(C)):  # 1
        for b in range(len(B)):  # 1
            if C[c] >= B[b]:
                del B[b]
                break
    count += 1
print(count)

