n, m = map(int, input().split())
num = 1
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
for i in range(n + m - 1):
    for j in range(n):
        for k in range(m):
            if j + k == i:
                arr[j][k] = num
                num += 1
for i in arr:
    for j in i:
        print(j, end = " ")
    print()