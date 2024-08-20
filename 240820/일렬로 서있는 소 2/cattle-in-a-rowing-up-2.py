n = int(input())
cnt = 0
arr = list(map(int, input().split()))
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if arr[i] <= arr[j] and arr[j] <= arr[k] and arr[i] <= arr[k]:
                cnt += 1
print(cnt)