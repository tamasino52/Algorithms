from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split(' ')))
arr.sort()

target = 0
for n in arr:
    if target + 1 >= n:
        target += n
    else:
        break
print(target + 1)


