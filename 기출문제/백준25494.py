from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    a, b, c = map(int, stdin.readline().split(' '))
    count = 0
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            for z in range(1, c + 1):
                 if x // y == y // z == z // x:
                     count += 1
    print(count)