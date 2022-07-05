from sys import stdin

N = int(stdin.readline())

for _ in range(N):
    a, b = map(int, stdin.readline().split(' '))
    a = a % 10

    if a == 1:
        print(1)
    elif a == 2:
        arr = [6, 2, 4, 8]
        print(arr[b % 4])
    elif a == 3:
        arr = [1, 3, 9, 7]
        print(arr[b % 4])
    elif a == 4:
        arr = [6, 4]
        print(arr[b % 2])

    elif a == 5:
        print(5)
    elif a == 6:
        print(6)
    elif a == 7:
        arr = [1, 7, 9, 3]
        print(arr[b % 4])

    elif a == 8:
        arr = [6, 8, 4, 2]
        print(arr[b % 4])
    elif a == 9:
        arr = [1, 9]
        print(arr[b % 2])
    elif a == 0:
        print(10)


