n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i == max(arr):
        cnt += 1
if cnt == 1:
    print(max(arr))
else:
    print(-1)