n = int(input())
arr = list(map(int, input().split()))
answer = 0
arr = arr[arr.index(min(arr)):]
if len(arr) == 1:
    print(0)
else:
    for i in arr:
        if i - min(arr) >= answer:
            answer = i - min(arr)
    print(answer)