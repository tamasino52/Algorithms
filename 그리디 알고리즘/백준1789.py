arr = input()
arr = [int(item) for item in arr]
arr.sort(reverse=True)
if 0 != arr[-1]:
    print(-1)
elif sum(arr) % 3 != 0:
    print(-2)
else:
    print(''.join([str(item) for item in arr]))