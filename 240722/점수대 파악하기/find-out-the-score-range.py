arr = list(map(int, input().split()))
count_arr = [0 for _ in range(11)]
for i in arr:
    if i == 0:
        break
    count_arr[i // 10] += 1
for i in range(10, 0, -1):
    print(f"{i}0 - {count_arr[i]}")