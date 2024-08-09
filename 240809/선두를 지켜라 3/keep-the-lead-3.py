n, m = map(int, input().split())
arr_a = [0]
cnt_a = 0
arr_b = [0]
cnt_b = 0
for _ in range(n):
    v, t = map(int, input().split())
    for i in range(t):
        cnt_a += v
        arr_a.append(cnt_a)
for _ in range(m):
    v, t = map(int, input().split())
    for i in range(t):
        cnt_b += v
        arr_b.append(cnt_b)
check_1st = 0
cnt_1st = 0
for i in range(1, len(arr_a)):
    if arr_a[i] > arr_b[i] and check_1st != 1:
        cnt_1st += 1
        check_1st = 1
    elif arr_a[i] < arr_b[i] and check_1st != -1:
        cnt_1st += 1
        check_1st = -1
    elif arr_a[i] == arr_b[i] and check_1st != 0:
        cnt_1st += 1
        check_1st = 0
print(cnt_1st)