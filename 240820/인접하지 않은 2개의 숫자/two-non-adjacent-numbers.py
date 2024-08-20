n = int(input())
arr = list(map(int, input().split()))
max_cnt = 0
for i in range(len(arr) - 2):
    for j in range(i + 2, len(arr)):
        max_cnt = max(max_cnt, arr[i] + arr[j])
print(max_cnt)