n = int(input())
a = 1
b = n
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j % 2 != 0:
            print(a, end = "")
        else:
            print(b, end = "")
    print()
    a += 1
    b -= 1