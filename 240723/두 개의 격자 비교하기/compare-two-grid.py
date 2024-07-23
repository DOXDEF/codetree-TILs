n, m = map(int, input().split())
answer = [
    [0 for _ in range(n)]
    for _ in range(m) 
]
arr_1 = [
    list(map(int, input().split()))
    for _ in range(m)
]
arr_2 = [
    list(map(int, input().split()))
    for _ in range(m)
]
for i in range(m):
    for j in range(n):
        if arr_1[i][j] != arr_2[i][j]:
            answer[i][j] = 1
for i in answer:
    for j in i:
        print(j, end = " ")
    print()