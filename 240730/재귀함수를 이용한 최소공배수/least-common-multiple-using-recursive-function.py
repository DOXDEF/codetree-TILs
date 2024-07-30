def div(arr, num, cnt):
    if arr.count(1) == cnt:
        return 1
    
    arr_dup = arr[:]
    for i in range(len(arr)):
        if arr[i] % num == 0:
            arr[i] //= num
    if arr_dup == arr:
        return div(arr, num + 1, cnt)
    else:
        return div(arr, num, cnt) * num

n = int(input())
arr = list(map(int, input().split()))
print(div(arr, 2, n))