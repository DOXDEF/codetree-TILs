def absolute(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

n = int(input())
arr = list(map(int, input().split()))
absolute(arr)
for i in arr:
    print(i, end = " ")