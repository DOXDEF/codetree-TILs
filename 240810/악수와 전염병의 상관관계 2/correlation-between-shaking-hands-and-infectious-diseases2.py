# 입력 받기
n, k, p, t = map(int, input().split())
timeline = []
arr_virus = [k for _ in range(n)]  # 각 개발자가 몇 번의 전염을 할 수 있는지 저장
arr_infect = [0 for _ in range(n)]  # 각 개발자가 전염되었는지 여부 저장
arr_infect[p - 1] = 1  # 초기 감염된 개발자

# 타임라인 입력
for _ in range(t):
    time, x, y = map(int, input().split())
    timeline.append([time, x - 1, y - 1])  # 인덱스를 맞추기 위해 1을 빼줌

# 시간순으로 정렬
timeline.sort()

# 타임라인 순서대로 처리
for event in timeline:
    time, x, y = event

    if arr_infect[x] == 1 and arr_infect[y] == 0 and arr_virus[x] > 0:
        arr_infect[y] = 1
        arr_virus[x] -= 1

    elif arr_infect[y] == 1 and arr_infect[x] == 0 and arr_virus[y] > 0:
        arr_infect[x] = 1
        arr_virus[y] -= 1

    elif arr_infect[x] == 1 and arr_infect[y] == 1:
        if arr_virus[x] > 0:
            arr_virus[x] -= 1
        if arr_virus[y] > 0:
            arr_virus[y] -= 1

# 결과 출력
for i in arr_infect:
    print(i, end="")