"""
백준 17472 : 다리 만들기 2 (골드1)
https://www.acmicpc.net/problem/17472
"""


from sys import stdin

# 지도의 가로 세로 크기 N,M
M, N = map(int, stdin.readline().split(' '))

mat = []
for _ in range(M):
    mat.append(list(map(int, stdin.readline().split(' '))))

island = 0
layers = [[0 for _ in range(N)] for _ in range(M)]

q = []
for r in range(M):
    for c in range(N):
        if (mat[r][c] == 1) and (layers[r][c] == 0):
            q.append((r, c))
            island += 1

        while len(q) > 0:
            y, x = q[0][0], q[0][1]
            q.pop(0)

            if 0 > y or y >= M or 0 > x or x >= N:
                continue

            if (mat[y][x] == 1) and (layers[y][x] == 0):
                layers[y][x] = island
                q.append((y+1, x))
                q.append((y-1, x))
                q.append((y, x+1))
                q.append((y, x-1))


visit = [[99 for _ in range(island)] for _ in range(island)]
import heapq

for r in range(M):
    for c in range(N):
        if layers[r][c] == 0:
            continue

        views = []
        views.append([layers[r][c + i] for i in range(N-c)])
        views.append([layers[r][c - i] for i in range(c)])
        views.append([layers[r + i][c] for i in range(M-r)])
        views.append([layers[r - i][c] for i in range(r)])

        for view in views:
            if len(view) > 2:
                for idx in range(1, len(view)):
                    if view[idx] > 0:
                        if idx >= 2:
                            visit[layers[r][c]-1][view[idx]-1] = min(idx, visit[layers[r][c]-1][view[idx]-1])
                            visit[view[idx]-1][layers[r][c]-1] = min(idx, visit[layers[r][c]-1][view[idx]-1])
                        break

connected = [0 for _ in range(island)]

res = 0

hp = []
for i in range(island):
    for j in range(island):
        if i > j:
            heapq.heappush(hp, (visit[i][j], i, j))

while sum(connected) < island - 1 and len(hp) > 0:
    cnt, i, j = heapq.heappop(hp)
    if connected[j] == 0:
        connected[j] = 1
        res += cnt
        print(i, j, cnt)
if sum(connected) < island - 1:
    print(-1)
else:
    print(res)



