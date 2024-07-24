arr = ["apple", "banana", "grape", "blueberry", "orange"]
n = input()
cnt = 0
for i in range(len(arr)):
    if arr[i][2] == n or arr[i][3] == n:
        print(arr[i])
        cnt += 1
print(cnt)