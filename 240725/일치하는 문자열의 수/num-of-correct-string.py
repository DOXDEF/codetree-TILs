n, m = map(str, input().split())
cnt = 0
for _ in range(int(n)):
    k = input()
    if m == k:
        cnt += 1
print(cnt)