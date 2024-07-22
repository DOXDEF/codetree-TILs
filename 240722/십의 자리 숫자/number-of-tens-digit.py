arr = list(map(int, input().split()))
count_arr = [0 for _ in range(10)]
for i in arr:
    if i == 0:
        break
    if i >= 10:
        count_arr[i // 10] += 1
for i in range(1, 10):
    print(f"{i} - {count_arr[i]}")