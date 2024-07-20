n = int(input())
for i in range(n):
    for j in range(n, i, -1):
        for k in range(n - i):
            print("*", end = "")
        print(" ", end = "")
    print()