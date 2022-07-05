from sys import stdin
import heapq
N = int(stdin.readline())
arr = []
# n log n
for _ in range(N):  # n
    s, t = map(int, stdin.readline().split(' '))
    arr.append((s, t))  # log n

arr.sort()
t_arr = []
heapq.heappush(t_arr, arr[0][1])
# n log n
for s, t in arr[1:]:  # n
    if t_arr[0] <= s:
        heapq.heappop(t_arr)  # log n
        heapq.heappush(t_arr, t)  # log n
    else:
        heapq.heappush(t_arr, t)  # log n

print(len(t_arr))

