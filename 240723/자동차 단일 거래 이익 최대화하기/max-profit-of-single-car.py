n = int(input())
arr = list(map(int, input().split()))
answer = 0
while True:
    if len(arr[arr.index(min(arr)):]) == 1:
        arr = arr[:arr.index(min(arr))]
    else:
        arr = arr[arr.index(min(arr)):]
        for i in arr:
            if i - min(arr) >= answer:
                answer = i - min(arr)
        print(answer)
        break