arr = [
    [0 for _ in range(2001)]
    for _ in range(2001)
]
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1 + 1000, x2 + 1000):
    for j in range(y1 + 1000, y2 + 1000):
        if arr[i][j] == 1:
            pass
        else:
            arr[i][j] = 1
a1, b1, a2, b2 = map(int, input().split())
for i in range(a1 + 1000, a2 + 1000):
        for j in range(b1 + 1000, b2 + 1000):
            if arr[i][j] == 0:
                pass
            else:
                arr[i][j] = 0
max_row = 0
row = 0
max_col = 0
for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 1:
            row += 1
    if row != 0:
        max_col += 1
    if row > max_row:
        max_row = row
    row = 0
print(max_row * max_col)