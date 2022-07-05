from sys import stdin
T = int(stdin.readline())

while T > 0:
    T -= 1

    N = int(input())

    count = 0
    min1 = N
    arr = [0] * N

    for _ in range(N):  # O(N)
        v1, v2 = list(map(int, stdin.readline().split()))
        #v1, v2 = map(int, input().split(' '))
        arr[v1 - 1] = v2 - 1  # O(1)

    for j in arr:  # O(N)
        if min1 > j:
            min1 = j
            count += 1
        if min1 == 0:
            break

    print(count)