n = int(input())
arr = list(map(int, input().split()))
answer = 0
buy = arr[0]
for i in range(n):
    if arr[i] <= buy:
            buy = arr[i]
    for j in range(i + 1, n):
        if arr[j] > buy and answer < arr[j] - buy:
            answer = arr[j] - buy
print(answer)