arr = list(map(int, input().split()))
answer = []
for i in arr:
    if i == 0:
        break
    else:
        answer.append(i)
print(answer[len(answer) - 1] + answer[len(answer) - 2] + answer[len(answer) - 3])