n1, n2 = map(int, input().split())
arr_n1 = list(map(int, input().split()))
arr_n2 = list(map(int, input().split()))
cnt = 0
if n1 >= n2:
    for i in range(n1 - n2 + 1):
        if arr_n1[i:n2 + i] == arr_n2:
            print("Yes")
            cnt = 1
            break
    if cnt == 0:
        print("No")
else:
    for i in range(n2 - n1 + 1):
        if arr_n2[i:n1 + i] == arr_n1:
            print("Yes")
            cnt = 1
            break
    if cnt == 0:
        print("No")