arr = list(map(int, input().split()))
answer = []
for i in arr:
    if i == 0:
        break
    else:
        answer.append(i)
for i in range(len(answer) - 1, -1, -1):
    print(answer[i], end = " ")