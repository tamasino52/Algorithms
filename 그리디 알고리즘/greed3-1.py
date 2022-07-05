# 그리디 알고리즘 연습
# 예제 3-1 거스름돈

N = int(input())
coins = [500, 100, 50, 10]
count = 0

for coin in coins:
    count += N // coin
    N %= coin
print(count)