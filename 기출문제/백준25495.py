from sys import stdin

N = int(stdin.readline())
A_list = map(int, stdin.readline().split(' '))

weight = 2
current = -1
count = 0
for A in A_list:
    if A != current:
        count += 2
        weight = 2
        current = A
    elif A == current:
        weight *= 2
        count += weight

    if count >= 100:
        count = 0
        current = -1
        weight = 2
print(count)

# 2 6 14 30 62 126 2
#