from sys import stdin
from queue import PriorityQueue

N = int(stdin.readline())
arr = PriorityQueue()
for _ in range(N):  # O(NlogN)
    v = int(stdin.readline())
    arr.put(v)  # O(logN)

count = 0
for _ in range(N-1):  # O(3NlogN)
    v1 = arr.get()  # O(logN)
    v2 = arr.get()  # O(logN)
    arr.put(v1+v2)  # O(logN)
    count += v1 + v2

print(count)