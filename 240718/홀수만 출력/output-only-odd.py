a, b = map(int, input().split())
for i in range(a, b + 1, 2):
    if (a % 2) == 0:
        print(i + 1, end = " ")
    else:
        print(i, end = " ")