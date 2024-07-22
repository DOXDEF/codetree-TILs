arr = list(map(int, input().split()))
answer = []
for i in arr:
    if i == 0:
        break
    else:
        answer.append(i)
print(f"{sum(answer)} {sum(answer) / len(answer):.1f}")