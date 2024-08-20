n = int(input())
arr_2d = []
cnt = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    arr_2d.append(arr)
for i in range(n):
    for j in range(n - 2):
        cnt = max(cnt, arr_2d[i][j] + arr_2d[i][j + 1] + arr_2d[i][j + 1])
print(cnt)