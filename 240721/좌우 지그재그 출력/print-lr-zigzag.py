n = int(input())
for i in range(n):
    if i % 2 == 0:
        for j in range(i * n + 1, n * (i + 1) + 1):
            print(j, end = " ")
    else:
        for j in range(n * (i + 1), i * n, -1):
            print(j, end = " ")
    print()