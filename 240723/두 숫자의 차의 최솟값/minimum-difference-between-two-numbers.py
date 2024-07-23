n = int(input())
arr = list(map(int, input().split()))
answer = 99
for i in range(n - 1):
    if arr[i + 1] - arr[i] <= answer:
        answer = arr[i + 1] - arr[i]
print(answer)