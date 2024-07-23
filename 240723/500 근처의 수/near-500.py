arr = list(map(int, input().split()))
max_arr = 0
min_arr = 1000
for i in arr:
    if i < 500 and i >= max_arr:
        max_arr = i
    elif i > 500 and i <= min_arr:
        min_arr = i
print(max_arr, min_arr)