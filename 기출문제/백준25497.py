from sys import stdin

N = int(stdin.readline())
skills = []
for _ in range(N):
    s = stdin.read(1)
    skills.append(s)

ready_l = 0
ready_s = 0

count = 0
for skill in skills:
    if skill == 'S':
        ready_s += 1
        continue
    if skill == 'L':
        ready_l += 1
        continue
    if skill == 'R' and ready_l == 0:
        break
    if skill == 'K' and ready_s == 0:
        break
    if skill == 'R' and ready_l > 0:
        ready_l -= 1
    if skill == 'K' and ready_s > 0:
        ready_s -= 1
    count += 1
print(count)
