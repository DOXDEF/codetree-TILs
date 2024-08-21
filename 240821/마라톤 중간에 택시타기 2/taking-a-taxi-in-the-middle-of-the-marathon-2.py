def calculate_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def find_min_distance(n, points):
    # 모든 체크포인트를 방문할 때의 총 거리
    total_distance = 0
    for i in range(1, n):
        total_distance += calculate_distance(points[i-1], points[i])
    
    # 체크포인트 하나를 건너뛰었을 때의 최소 거리 계산
    min_distance = float('inf')
    for i in range(1, n-1):  # 2번 체크포인트부터 N-1번 체크포인트 중 하나를 건너뜀
        distance_with_skip = total_distance
        distance_with_skip -= calculate_distance(points[i-1], points[i])
        distance_with_skip -= calculate_distance(points[i], points[i+1])
        distance_with_skip += calculate_distance(points[i-1], points[i+1])
        
        min_distance = min(min_distance, distance_with_skip)
    
    return min_distance

# 입력
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 최소 거리 계산 및 출력
result = find_min_distance(n, points)
print(result)