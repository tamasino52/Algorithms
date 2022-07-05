N = int(input())
dists = list(map(int, input().split(' ')))
prices = list(map(int, input().split(' ')))

price_list = []
min_price = 1000000001

for price in prices:
    if min_price > price:
        min_price = price
    price_list.append(min_price)

res = 0
for i in range(len(dists)):
    res += dists[i] * price_list[i]

print(res)