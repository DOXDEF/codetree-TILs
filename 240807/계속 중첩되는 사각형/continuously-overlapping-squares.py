arr = [
    [0 for _ in range(201)]
    for _ in range(201)
]
n = int(input())
cnt = 0
for k in range(n):
    if k % 2 == 0:
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1 + 100, x2 + 100):
            for j in range(y1 + 100, y2 + 100):
                if arr[i][j] == 2:
                    cnt -= 1
                arr[i][j] = 1
    else:
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1 + 100, x2 + 100):
            for j in range(y1 + 100, y2 + 100):
                if arr[i][j] == 2:
                    pass
                else:
                    arr[i][j] = 2
                    cnt += 1
print(cnt)