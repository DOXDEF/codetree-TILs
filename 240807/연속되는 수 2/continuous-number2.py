n = int(input())
combo = 0
cnt = 1
max_cnt = 0
for _ in range(n):
    a = int(input())
    if combo != a:
        combo = a
        if max_cnt < cnt:
            max_cnt = cnt
        cnt = 1
    else:
        cnt += 1
if max_cnt < cnt:
    max_cnt = cnt
print(max_cnt)