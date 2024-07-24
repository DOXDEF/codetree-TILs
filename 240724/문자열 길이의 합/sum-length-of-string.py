n = int(input())
arr = [
    list(input())
    for _ in range(n)
]
sum_len = 0
cnt = 0
for i in arr:
    sum_len += len(i)
    cnt += i.count('a')
print(sum_len, cnt)