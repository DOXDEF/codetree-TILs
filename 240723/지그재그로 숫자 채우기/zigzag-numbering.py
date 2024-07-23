n, m = map(int, input().split())
num = 0
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            arr[j][i] = num
            num += 1
    else:
        for j in range(n - 1, -1, -1):
            arr[j][i] = num
            num += 1
for i in arr:
    for j in i:
        print(j, end = " ")
    print()