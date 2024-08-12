n, t = map(int, input().split())
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]
r, c, d = map(str, input().split())
r, c = int(r) - 1, int(c) - 1
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}
move_dir = mapper[d]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(t):
    if d == 'R':
        nr, nc = r + dxs[move_dir], c + dys[move_dir]
        if not in_range(nr, nc):
            d = 'L'
            move_dir = mapper[d]
            continue
        r, c = r + dxs[move_dir], c + dys[move_dir]
    elif d == 'L':
        nr, nc = r + dxs[move_dir], c + dys[move_dir]
        if not in_range(nr, nc):
            d = 'R'
            move_dir = mapper[d]
            continue
        r, c = r + dxs[move_dir], c + dys[move_dir]
    elif d == 'U':
        nr, nc = r + dxs[move_dir], c + dys[move_dir]
        if not in_range(nr, nc):
            d = 'D'
            move_dir = mapper[d]
            continue
        r, c = r + dxs[move_dir], c + dys[move_dir]
    elif d == 'D':
        nr, nc = r + dxs[move_dir], c + dys[move_dir]
        if not in_range(nr, nc):
            d = 'U'
            move_dir = mapper[d]
            continue
        r, c = r + dxs[move_dir], c + dys[move_dir]

print(r + 1, c + 1)