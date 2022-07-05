from sys import stdin
import heapq

N, K = map(int, stdin.readline().split(' '))
k_arr = list(map(int, stdin.readline().split(' ')))

arr = []
count = 0
for k in range(len(k_arr)):
    if k_arr[k] in arr:
        continue
    else:
        if len(arr) < N:
            arr.append(k_arr[k])
        else:
            max_p = 0
            idx_p = 0

            for idx, p in enumerate(arr):
                try:
                    i = k_arr[k+1:].index(p)
                except ValueError:
                    idx_p = idx
                    break
                if max_p < i:
                    idx_p = idx
                    max_p = i

            del arr[idx_p]
            arr.append(k_arr[k])
            count += 1
print(count)

