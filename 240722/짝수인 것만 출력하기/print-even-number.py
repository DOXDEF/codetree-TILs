n = int(input())
arr = list(map(int, input().split()))
answer = []
for i in arr:
    if i % 2 == 0:
        answer.append(i)
for i in answer:
    print(i, end = " ")