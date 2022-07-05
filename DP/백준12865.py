from sys import stdin

N, K = map(int, stdin.readline().split(' '))

W, V = [], []
for _ in range(N):
    w, v = map(int, stdin.readline().split(' '))
    W.append(w)
    V.append(v)

arr = {K: 0}
for w, v in zip(W, V):
    for s_k, s_v in list(arr.items()):
        if s_k - w < 0:
            continue
        if s_k - w in arr.keys():
            arr[s_k - w] = max(s_v + v, arr[s_k - w])
        else:
            arr[s_k - w] = s_v + v

print(max(arr.values()))
