arr = list(map(int, input().split()))
answer = []
for i in arr:
    if i == 0:
        break
    else:
        answer.append(i)
for i in answer:
    if i % 2 == 0:
        print(i // 2, end = " ")
    else:
        print(i + 3, end = " ")