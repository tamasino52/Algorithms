from sys import stdin
from queue import PriorityQueue

N, K = map(int, stdin.readline().split(' '))
arr = PriorityQueue()

C = []
for _ in range(N):  # n
    m, v = map(int, stdin.readline().split(' '))
    arr.put((-v, m))  # log n

for _ in range(K):
    c = int(stdin.readline())
    C.append(c)

C.sort()  # nlogn
count = 0

for c in C:  # n
    max_v = 0
    max_i = -1

    while True:
        v, m = arr.get()  # log n
        if c >= m:
            count += -v
            break
        else:
            arr.put((v, m))  # log n

print(count)




