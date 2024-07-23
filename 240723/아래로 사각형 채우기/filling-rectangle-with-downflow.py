n = int(input())
num = 1
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]
for i in range(n):
    arr[i][0] = num
    for j in range(1, n):
        arr[i][j] = num + (n * j)
    num += 1
for i in arr:
    for j in i:
        print(j, end = " ")
    print()