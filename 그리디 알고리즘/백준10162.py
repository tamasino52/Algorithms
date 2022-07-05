T = int(input())
res1, res2, res3 = 0, 0, 0

if T % 10 > 0:
    print(-1)
else:
    arr = [300, 60, 10]
    res1 += T // 300
    T = T % 300

    res2 += T // 60
    T = T % 60

    res3 += T // 10
    T = T % 10

    print(res1, res2, res3)