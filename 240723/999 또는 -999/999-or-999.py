arr = list(map(int, input().split()))
answer = []
for i in arr:
    if i == 999 or i == -999:
        break
    answer.append(i)
print(max(answer), min(answer))