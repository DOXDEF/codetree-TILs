arr = [1]
n = int(input())
arr.append(n)
for i in range(20):
    arr.append(arr[i] + arr[i + 1])
    if arr[i] + arr[i + 1] >= 100:
        break
for i in arr:
    print(i, end = " ")