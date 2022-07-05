from sys import stdin

N = int(stdin.readline())
dic = {}

for _ in range(N):
    word_list = list(stdin.readline())
    word_list.pop()

    for i, word in enumerate(word_list):
        if word in dic.keys():
            dic[word] += 10 ** (len(word_list) - i - 1)
        else:
            dic[word] = 10 ** (len(word_list) - i - 1)

arr = list(dic.values())
arr.sort(reverse=True)

count = 0
for idx, num in enumerate(arr):
    count += num * (9-idx)
print(count)