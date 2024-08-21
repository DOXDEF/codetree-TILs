def min_marathon_distance(checkpoints):
    n = len(checkpoints)
    distance = [[0] * n for _ in range(n)]

    # 각 체크포인트 간의 거리를 계산하여 distance 배열에 저장
    for i in range(n):
        for j in range(n):
            x1, y1 = checkpoints[i]
            x2, y2 = checkpoints[j]
            distance[i][j] = abs(x1 - x2) + abs(y1 - y2)

    # 최소 거리 찾기
    min_distance = float('inf')
    for i in range(1, n - 1):
        total_distance = sum(distance[j][k] for j in range(i) for k in range(i + 1, n))
        min_distance = min(min_distance, total_distance)

    return min_distance

n = int(input())
checkpoints = []
for _ in range(n):
    a, b = map(int, input().split())
    checkpoints.append((a, b))
print(min_marathon_distance(checkpoints))  # 출력: 14