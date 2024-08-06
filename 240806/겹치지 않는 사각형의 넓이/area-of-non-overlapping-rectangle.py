arr = [
    [0 for _ in range(2001)]
    for _ in range(2001)
]
cnt = 0
for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 + 1000, x2 + 1000):
        for j in range(y1 + 1000, y2 + 1000):
            if arr[i][j] == 1:
                pass
            else:
                arr[i][j] = 1
                cnt += 1
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1 + 1000, x2 + 1000):
        for j in range(y1 + 1000, y2 + 1000):
            if arr[i][j] == 0:
                pass
            else:
                arr[i][j] = 0
                cnt -= 1
print(cnt)