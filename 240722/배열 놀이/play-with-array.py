n, q = map(int, input().split())
cnt = 0
arr = list(map(int, input().split()))
for _ in range(q):
    count_arr = list(map(int, input().split()))
    if count_arr[0] == 1:
        print(arr[count_arr[1] - 1])
    elif count_arr[0] == 2:
        for i in range(len(arr)):
            if arr[i] == count_arr[1]:
                print(i + 1)
                cnt = 1
                break
        if cnt == 0:
            print(0)
        cnt = 0
    else:
        for i in range(count_arr[1] - 1, count_arr[2]):
            print(arr[i], end = " ")
        print()