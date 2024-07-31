n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = []
for i in range(n):
    answer.append(arr[i] + arr[n * 2 - (i + 1)])
answer.sort(reverse = True)
print(answer[0])