n = int(input())
cnt = 0
for i in range(1, n + 1):
    if i == 1:
        for j in range(n):
            print("*", end = " ")
        print()
        cnt += 1
    else:
        for j in range(1, n + 1):
            if j % 2 == 0 and cnt < j:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        cnt += 1
        print()