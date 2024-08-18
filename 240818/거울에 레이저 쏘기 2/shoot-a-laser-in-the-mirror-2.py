def simulate_laser(grid, start_pos, N):
    # 방향 정의: (dx, dy)
    directions = {
        'up': (-1, 0), 
        'down': (1, 0), 
        'left': (0, -1), 
        'right': (0, 1)
    }
    
    # 시작 위치에 따른 초기 방향 설정
    if 1 <= start_pos <= N:
        x, y, direction = 0, start_pos - 1, 'down'
    elif N + 1 <= start_pos <= 2 * N:
        x, y, direction = start_pos - N - 1, N - 1, 'left'
    elif 2 * N + 1 <= start_pos <= 3 * N:
        x, y, direction = N - 1, 3 * N - start_pos, 'up'
    else:
        x, y, direction = 4 * N - start_pos, 0, 'right'

    count = 0
    
    while 0 <= x < N and 0 <= y < N:
        count += 1
        if grid[x][y] == '/':
            if direction == 'up':
                direction = 'right'
            elif direction == 'down':
                direction = 'left'
            elif direction == 'left':
                direction = 'down'
            elif direction == 'right':
                direction = 'up'
        elif grid[x][y] == '\\':
            if direction == 'up':
                direction = 'left'
            elif direction == 'down':
                direction = 'right'
            elif direction == 'left':
                direction = 'up'
            elif direction == 'right':
                direction = 'down'
        
        dx, dy = directions[direction]
        x += dx
        y += dy

    return count

# 입력 받기
N = int(input())
grid = [input().strip() for _ in range(N)]
K = int(input())

# 결과 출력
result = simulate_laser(grid, K, N)
print(result)