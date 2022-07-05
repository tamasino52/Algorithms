from sys import stdin

R, C = map(int, stdin.readline().split(' '))
arr = []
for r in range(R):
    arr.append(list(stdin.readline().rstrip("\n")))

count = 0
for r in range(R):  # n
    for c in range(C):
        arr[r][c] = 'x'
        if c == C-1:
            count += 1
            break
        elif r > 0 and arr[r-1][c+1] == '.':
            r -= 1
        elif arr[r][c+1] == '.':
            continue
        elif r < R-1 and arr[r+1][c+1] == '.':
            r += 1
        else:
            break
print(count)
