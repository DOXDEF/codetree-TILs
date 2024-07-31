n = int(input())
arr = list(map(int, input().split()))
answer = []
for i in range(len(arr)):
    answer.append(arr[i])
    if i % 2 == 0:
        answer.sort()
        print(answer[i // 2], end = " ")