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
tangle_row = []
tangle_col = []
for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 1:
            tangle_col.append(i)
            tangle_row.append(j)
tangle_col.sort()
tangle_row.sort()
if len(tangle_col) == 0 and len(tangle_row) == 0:
    print(0)
else:
    print((tangle_col[len(tangle_col) - 1] - tangle_col[0] + 1) * (tangle_row[len(tangle_row) - 1] - tangle_row[0] + 1))