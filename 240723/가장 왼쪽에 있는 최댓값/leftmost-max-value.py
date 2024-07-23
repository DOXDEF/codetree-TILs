n = int(input())
arr = list(map(int, input().split()))
while True:
    print(arr.index(max(arr)) + 1, end = " ")
    if arr.index(max(arr)) == 0:
        break
    arr = arr[:arr.index(max(arr))]