n = int(input())
arr = [
    list(input())
    for _ in range(n)
]
sum_len = 0
cnt = 0
for i in arr:
    sum_len += len(i)
    if i[0] == 'a':
        cnt += 1
print(sum_len, cnt)