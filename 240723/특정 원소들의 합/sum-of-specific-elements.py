arr_2d = []
answer = 0
for i in range(4):
    arr = list(map(int, input().split()))
    arr_2d.append(arr)
for i in range(4):
    for j in range(0, i + 1):
        answer += arr_2d[i][j]
print(answer)