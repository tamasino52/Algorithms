N = int(input())

count = N // 5
res = None

for i in reversed(range(count + 1)):
    last = N - 5 * i

    if last % 3 == 0:
        res = i + last // 3
        print(res)
        break

if res is None:
    print(-1)