N, M = map(int, input().split(' '))
arr2 = []
for _ in range(N):
    arr1 = list(map(int, input().split(' ')))
    arr2.append(min(arr1))

print(max(arr2))

