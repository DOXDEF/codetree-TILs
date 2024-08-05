arr = [0] * 200001
arr_cnt = [0] * 200001
point = 100000
n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    if b == 'R':
        for i in range(point, point + int(a)):
            arr[i] = 1
            arr_cnt[i] += 1
            if arr_cnt[i] >= 4:
                arr[i] = 0
        point += (int(a) - 1)
    else:
        for i in range(point, point - int(a), -1):
            arr[i] = -1
            arr_cnt[i] += 1
            if arr_cnt[i] >= 4:
                arr[i] = 0
        point -= (int(a) - 1)
gray = 0
arr_cnt.sort(reverse = True)
for i in range(len(arr_cnt)):
    if arr_cnt[i] >= 4:
        gray += 1
    else:
        break
print(arr.count(-1), arr.count(1), gray)