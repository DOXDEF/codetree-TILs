n = int(input())
arr = []
part = []
sign = 0
cnt = 0
for _ in range(n):
    a = int(input())
    arr.append(a)
for i in range(len(arr)):
    if arr[i] > 0:
        if sign == 1:
            cnt += 1
        else:
            part.append(cnt)
            sign = 1
            cnt = 1
    else:
        if sign == -1:
            cnt += 1
        else:
            part.append(cnt)
            sign = -1
            cnt = 1
part.append(cnt)
part.sort(reverse = True)
print(part[0])