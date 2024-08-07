n = int(input())
arr = []
part = []
cnt = 1
for _ in range(n):
    a = int(input())
    arr.append(a)
for i in range(1, len(arr)):
    if arr[i - 1] < arr[i]:
        cnt += 1
    else:
        part.append(cnt)
        cnt = 1
part.append(cnt)
part.sort(reverse = True)
print(part[0])