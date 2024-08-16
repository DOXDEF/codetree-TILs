n = int(input())
answer = [
    [0] * n
    for _ in range(n)
]
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
x, y = n // 2, n // 2  # 시작은 (0, 0) 입니다.
dir_num = -1  # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
# 처음 시작 위치에 초기값을 적습니다.
answer[x][y] = 1
cnt = 1
# 나선형으로 n * m번 진행합니다.
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
for i in range(1, n * 2 + 1):
        for j in range(i // 2):
            # 현재 방향 dir를 기준으로 그 다음 위치 값을 계산합니다
            nx, ny = x + dxs[dir_num], y + dys[dir_num]
            if in_range(nx, ny):
                x, y = x + dxs[dir_num], y + dys[dir_num]
                cnt += 1
                answer[x][y] = cnt
        dir_num = (dir_num + 1) % 4
    

# 출력:
for i in range(n):
    for j in range(n):
        print(answer[i][j], end=' ')
    print()