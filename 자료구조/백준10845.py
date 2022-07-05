from sys import stdin
from queue import Queue

N = int(stdin.readline())
arr = Queue()
t = 0

for _ in range(N):
    oper = list(stdin.readline().split(' '))
    if len(oper) > 1:
        t = int(oper[1])
        oper = oper[0]
    else:
        oper = oper[0][:-1]

    if oper == 'push':
        arr.put(t)
    elif oper == 'front':
        print(arr.queue[0] if not arr.empty() else -1)
    elif oper == 'back':
        print(arr.queue[-1] if not arr.empty() else -1)
    elif oper == 'empty':
        print(1 if arr.empty() else 0)
    elif oper == 'size':
        print(arr.qsize())
    elif oper == 'pop':
        print(arr.get() if not arr.empty() else -1)