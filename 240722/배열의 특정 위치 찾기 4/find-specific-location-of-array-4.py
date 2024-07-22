arr = list(map(int, input().split()))
answer = []
cnt = 0
sum_2 = 0
for i in arr:
    if i == 0:
        break
    else:
        answer.append(i)
for i in answer:
    if i % 2 == 0:
        cnt += 1
        sum_2 += i
print(cnt, sum_2)