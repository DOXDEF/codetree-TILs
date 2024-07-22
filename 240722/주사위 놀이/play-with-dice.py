arr = list(map(int, input().split()))
count_arr = [0 for i in range(7)]
for i in arr:
    count_arr[i] += 1
for i in range(1, 7):
    print(f"{i} - {count_arr[i]}")