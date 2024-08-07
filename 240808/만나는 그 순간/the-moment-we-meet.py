n, m = map(int, input().split())
arr_a = [0]
arr_b = [0]
cnt_a = 0
cnt_b = 0
for _ in range(n):
    d, t = map(str, input().split())
    if d == 'R':
        for i in range(int(t)):
            cnt_a += 1
            arr_a.append(cnt_a)
    else:
        for i in range(int(t)):
            cnt_a -= 1
            arr_a.append(cnt_a)
for _ in range(m):
    d, t = map(str, input().split())
    if d == 'R':
        for i in range(int(t)):
            cnt_b += 1
            arr_b.append(cnt_b)
    else:
        for i in range(int(t)):
            cnt_b -= 1
            arr_b.append(cnt_b)
answer = -1
for i in range(1, len(arr_a)):
    if arr_a[i] == arr_b[i]:
        answer = i
        break
print(answer)