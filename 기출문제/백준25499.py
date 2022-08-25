from sys import stdin

N = int(stdin.readline())
A_list = list(map(int, stdin.readline().split(' ')))
#111111

def fn(start, end):
    if start == end:
        return 0
    count = [end-start]
    for idx in range(start, end):  # n
        A = A_list[idx]
        if A > 0:
            # 왼쪽 넘어짐
            if start <= idx - A and max(A_list[idx-A:idx]) == 0:  # n
                A_list[idx] = 0
                left = idx - A + fn(idx, end)
                count.append(left)
                A_list[idx] = A
            # 가만히
            center = idx + fn(idx + 1, end)
            count.append(center)
            # 오른쪽 넘어짐
            if idx+A < end and max(A_list[idx+1:idx+A+1]) == 0:  # n
                right = idx + 1 + fn(idx+A+1, end)
                count.append(right)
            break
    return min(count)


print(fn(0, N))