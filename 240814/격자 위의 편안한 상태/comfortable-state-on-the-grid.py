n, m = map(int, input().split())
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(m):
    x, y = map(int, input().split())
    arr_2d[x - 1][y - 1] = 1
    cnt = 0
    cnt_one = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x - 1 + dx, y - 1 + dy
        if in_range(nx, ny) and arr_2d[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        cnt_one = 1
    print(cnt_one)