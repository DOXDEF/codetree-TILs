n, m = map(int, input().split())
answer = [
    [0] * m
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0  # 시작은 (0, 0) 입니다.
dir_num = 0  # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽

# 처음 시작 위치에 초기값을 적습니다.
answer[x][y] = 'A'

# 나선형으로 n * m번 진행합니다.
for i in range(1, n * m):
    # 현재 방향 dir를 기준으로 그 다음 위치 값을 계산합니다.
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    # 더 이상 나아갈 수 없다면 시계방향으로 90도 회전합니다.
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

    # 그 다음 위치로 이동한 다음 배열에 올바른 값을 채워넣습니다.
    x, y = nx, ny
    answer[x][y] = chr(ord('A') + (i % 26))

# 출력:
for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()