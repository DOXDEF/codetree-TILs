n = int(input())
for i in range(n - 1, -1, -1):
    for j in range(i):
        print(" ", end = " ")
    for j in range(n * 2 - 1 - i * 2):
        print("*", end = " ")
    print()