n = int(input())
num = 11
for i in range(n):
    for j in range(n):
        print(num + j * 2, end = " ")
    print()
    num += 2