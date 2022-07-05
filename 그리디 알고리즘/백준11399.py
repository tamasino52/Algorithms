N = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

res = 0
for i in range(N):
    res += sum(arr[:i+1])

print(res)
