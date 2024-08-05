arr = [0] * 200001
arr_cnt = [0] * 200001
point = 100000
n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    if b == 'R':
        for i in range(int(a)):
            arr[point] = 1
            arr_cnt[point] += 1
            if arr_cnt[point] >= 4:
                arr[point] = 0
            point += 1
    else:
        for i in range(int(a)):
            point -= 1
            arr[point] = -1
            arr_cnt[point] += 1
            if arr_cnt[point] >= 4:
                arr[point] = 0
gray = 0
arr_cnt.sort(reverse = True)
for i in range(len(arr_cnt)):
    if arr_cnt[i] >= 4:
        gray += 1
    else:
        break
print(arr.count(-1), arr.count(1), gray)