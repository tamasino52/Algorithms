a = input()
arr = list(map(int, sum([item.split('-') for item in a.split('+')], [])))
oper = []
for i in a:
    if i == '+' or i == '-':
        oper.append(i)

res = arr[0]
sign = 1
for num, op in zip(arr[1:], oper):
    if op == '-':
        sign = -1
    res += num * sign
print(res)
