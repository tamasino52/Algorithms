N, M, K = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr.sort()

v1 = arr[-1]
v2 = arr[-2]
res = 0

a = M // (K+1)
res += a * K * v1
res += a * v2

b = M % (K+1)
res += b * v1

print(res)