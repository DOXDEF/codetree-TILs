count_arr = [0 for _ in range(4)]
for _ in range(3):
    a, b = map(str, input().split())
    if a == 'Y':
        if int(b) >= 37:
            count_arr[0] += 1
        else:
            count_arr[2] += 1
    else:
        if int(b) >= 37:
            count_arr[1] += 1
        else:
            count_arr[3] += 1
for i in range(4):
    print(count_arr[i], end = " ")
if count_arr[0] >= 2:
    print('E', end = " ")