N, K = map(int, input().split(' '))
arr = []
for _ in range(N):
    tmp = int(input())
    arr.append(tmp)

count = 0

for coin in reversed(arr):
    if K >= coin:
        count += K // coin
        K = K % coin

print(count)