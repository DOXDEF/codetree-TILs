arr = [
    [0 for _ in range(201)]
    for _ in range(201)
]
n = int(input())
cnt = 0
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x + 100, x + 108):
        for j in range(y + 100, y + 108):
            if arr[i][j] == 1:
                pass
            else:
                arr[i][j] = 1
                cnt += 1
print(cnt)