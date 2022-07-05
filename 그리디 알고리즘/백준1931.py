import queue

prior = queue.PriorityQueue()
N = int(input())

for _ in range(N):
    v1, v2 = map(int, input().split(' '))
    prior.put((v2, v1))

end = 0
count = 0
while not prior.empty():
    v2, v1 = prior.get()
    if end > v1:
        continue
    count += 1
    end = v2

print(count)
