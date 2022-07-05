from sys import stdin

from queue import Queue

N, K = map(int, stdin.readline().split(' '))
arr = list(map(int, list(stdin.readline().rstrip('\n'))))

num_q = []

start = 0
while K > 0:  # n
    K -= 1
    for i in range(start, len(arr)):  # n
        if arr == len(arr)-1:
            arr.pop(-1)
            break
        if arr[i+1] > arr[i]:
            arr.pop(i)  # n
            start = max(i-1, 0)
            break

count = 0
for num in arr: # n
    count *= 10
    count += num
print(count)