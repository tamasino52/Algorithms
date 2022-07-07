"""
백준 14502번 : 연구소 (골드5)
https://www.acmicpc.net/problem/14502
"""

from sys import stdin
from copy import deepcopy


def virus(y, x, arr):
    if y<0 or x<0:
        return
    try:
        if arr[y][x] == 0:
            arr[y][x] = 2
            for off in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                virus(y+off[0], x+off[1], arr)
        elif arr[y][x] == 1:
            return
        elif arr[y][x] == 2:
            return
    except IndexError:
        return


N, M = map(int, stdin.readline().split(' '))
arr = [0 for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, stdin.readline().split(' ')))

v_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            v_list.append((i,j))

points = []
max_area = 0
for t1 in range(N * M - 2):
    for t2 in range(t1 + 1, N * M - 1):
        for t3 in range(t2 + 1, N * M):

            p1 = (t1 // M, t1 % M)
            p2 = (t2 // M, t2 % M)
            p3 = (t3 // M, t3 % M)

            if arr[p1[0]][p1[1]] == 0 and arr[p2[0]][p2[1]] == 0 and arr[p3[0]][p3[1]] == 0:
                arr[p1[0]][p1[1]] = 1
                arr[p2[0]][p2[1]] = 1
                arr[p3[0]][p3[1]] = 1

                visit = deepcopy(arr)
                for i, j in v_list:
                    visit[i][j] = 0
                    virus(i, j, visit)

                count = 0
                for i in range(N):
                    for j in range(M):
                        if visit[i][j] == 0:
                            count += 1

                if count > max_area:
                    max_area = count

                arr[p1[0]][p1[1]] = 0
                arr[p2[0]][p2[1]] = 0
                arr[p3[0]][p3[1]] = 0
            else:
                continue
print(max_area)




