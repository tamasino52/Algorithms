from sys import stdin

P, N = map(int, stdin.readline().split(' '))
A_list = list(map(int, stdin.readline().split(' ')))

A_list.sort()

count = 0
for A in A_list:
    if P >= 200:
        break
    P += A
    count += 1
print(count)