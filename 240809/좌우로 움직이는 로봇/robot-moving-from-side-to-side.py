n, m = map(int, input().split())
arr_a = [0]
cnt_a = 0
arr_b = [0]
cnt_b = 0
for _ in range(n):
    t, d = map(str, input().split())
    if d == 'R':
        for _ in range(int(t)):
            cnt_a += 1
            arr_a.append(cnt_a)
    else:
        for _ in range(int(t)):
            cnt_a -= 1
            arr_a.append(cnt_a)
for _ in range(m):
    t, d = map(str, input().split())
    if d == 'R':
        for _ in range(int(t)):
            cnt_b += 1
            arr_b.append(cnt_b)
    else:
        for _ in range(int(t)):
            cnt_b -= 1
            arr_b.append(cnt_b)
if len(arr_a) < len(arr_b):
    for _ in range(len(arr_b) - len(arr_a)):
        arr_a.append(arr_a[len(arr_a) - 1])
else:
    for _ in range(len(arr_a) - len(arr_b)):
        arr_b.append(arr_b[len(arr_b) - 1])
answer = 0
for i in range(1, len(arr_a)):
    if arr_a[i] == arr_b[i] and arr_a[i - 1] != arr_b[i - 1]:
        answer += 1
print(answer)