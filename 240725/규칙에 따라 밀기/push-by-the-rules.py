arr = list(input())
arr_com = list(input())
for i in arr_com:
    if i == 'L':
        arr = arr[1:] + arr[0:1]
    else:
        arr = arr[len(arr) - 1:] + arr[0:len(arr) - 1]
print("".join(arr))