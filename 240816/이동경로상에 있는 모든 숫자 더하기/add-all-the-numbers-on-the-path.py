n, t = map(int, input().split())
direction = input()
arr_2d = []
for _ in range(n):
    arr = list(map(int, input().split()))
    arr_2d.append(arr)

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
idx = 100000
x, y = n // 2, n // 2
sum_arr = arr_2d[x][y]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for i in range(len(direction)):
    if direction[i] == 'L':
        idx -= 1
    elif direction[i] == 'R':
        idx += 1
    elif direction[i] == 'F':
        nx, ny = x + dx[idx % 4], y + dy[idx % 4]
        if in_range(nx, ny):
            x, y = x + dx[idx % 4], y + dy[idx % 4]
            sum_arr += arr_2d[x][y]
print(sum_arr)