N = int(input())
arr = []

for _ in range(N):
    tmp = int(input())
    arr.append(tmp)

arr.sort()
size = len(arr)
max_w = arr[0] * size


for i in range(size):
    cur_w = arr[i] * (size-i)
    if max_w < cur_w:
        max_w = cur_w
print(max_w)

