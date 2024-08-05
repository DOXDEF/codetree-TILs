arr = [0] * 200001
cnt_black = [0] * 200001
cnt_white = [0] * 200001
point = 100000
n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    if b == 'R':
        for i in range(point, point + int(a)):
            arr[i] = 1
            cnt_black[i] += 1
            if cnt_white[i] + cnt_black[i] >= 4 and (cnt_black[i] >= 2 and cnt_white[i] >= 2):
                arr[i] = 2
        point += (int(a) - 1)
    else:
        for i in range(point, point - int(a), -1):
            arr[i] = -1
            cnt_white[i] += 1
            if cnt_white[i] + cnt_black[i] >= 4 and (cnt_black[i] >= 2 and cnt_white[i] >= 2):
                arr[i] = 2
        point -= (int(a) - 1)
print(arr.count(-1), arr.count(1), arr.count(2))