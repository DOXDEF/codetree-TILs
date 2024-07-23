n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr, reverse = True)
max_arr = -1
for i in arr:
    if arr.count(i) == 1 and i >= max_arr:
        max_arr = i
print(max_arr)