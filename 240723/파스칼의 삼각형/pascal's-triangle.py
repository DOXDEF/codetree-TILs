#(i, j)에 적힌 숫자가 
#(i - 1, j - 1)에 적힌 숫자와 (i - 1, j)에 적힌 숫자의 합으로 나타납니다.
n = int(input())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]
for i in range(n):
    arr[i][0] = 1
    arr[i][i] = 1
for i in range(2, n):
    for j in range(1, n):
        arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
for i in arr:
    for j in i:
        if j == 0:
            pass
        else:
            print(j, end = " ")
    print()