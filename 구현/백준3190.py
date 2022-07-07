"""
백준 3190번 : 뱀 (골드4)
https://www.acmicpc.net/problem/3190
"""

from sys import stdin


N = int(stdin.readline())  # 2 < < 100
K = int(stdin.readline())  # < 100
apples = []
for _ in range(K):
    r, c = map(int, stdin.readline().split(' '))
    apples.append((r, c))
L = int(stdin.readline())  # < 100
turns = []
for _ in range(L):
    opr = stdin.readline().split(' ')
    turns.append((int(opr[0]), opr[1][:-1]))  # X < 10000

arr = [[0 for _ in range(N)] for _ in range(N)]
for apple in apples:
    r, c = apple[0], apple[1]
    arr[r][c] = 2

body = [(0, 0)]
dir = 0
time = 0

while True:
    if len(turns) > 0:
        timing, opr = turns[0][0], turns[0][1]
        if time == timing:
            if opr == 'L':
                dir = (dir - 1) % 4
            elif opr == 'D':
                dir = (dir + 1) % 4
            turns.pop(0)

    if dir == 0:
        r, c = body[-1][0], body[-1][1] + 1
    elif dir == 2:
        r, c = body[-1][0], body[-1][1] - 1
    elif dir == 1:
        r, c = body[-1][0] + 1, body[-1][1]
    elif dir == 3:
        r, c = body[-1][0] - 1, body[-1][1]

    # 외벽 충돌 검사
    if c >= N or c < 0 or r < 0 or r >= N:
        print(time)
        exit()
    # 자기 충돌 검사
    if (r, c) in body:
        print(time)
        exit()
    # 전진
    if arr[r][c] == 0:
        body.append((r, c))
        body.pop(0)
    # 사과 먹음
    elif arr[r][c] == 2:
        arr[r][c] = 0
        body.append((r, c))
    time += 1
