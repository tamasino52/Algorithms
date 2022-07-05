from sys import stdin
import heapq

N = int(stdin.readline())
pos_arr, neg_arr = [], []
# n log n
for _ in range(N):  # n
    n = int(stdin.readline())
    if n > 0:
        heapq.heappush(pos_arr, -n)  # log n
    else:
        heapq.heappush(neg_arr, n)  # log n

total = 0

# n log n
while len(pos_arr) > 0:  # n
    v1 = -heapq.heappop(pos_arr)  # log n
    if len(pos_arr) > 0 and v1 * -pos_arr[0] > v1 + -pos_arr[0]:
        v2 = -heapq.heappop(pos_arr)  # log n
        total += v1 * v2
    else:
        total += v1

# n log n
while len(neg_arr) > 0:  # n
    v1 = heapq.heappop(neg_arr)  # log n
    if len(neg_arr) > 0 and v1 * neg_arr[0] > v1 + neg_arr[0]:
        v2 = heapq.heappop(neg_arr)  # log n
        total += v1 * v2
    else:
        total += v1
print(total)

