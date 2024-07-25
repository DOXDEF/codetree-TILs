arr = []
while True:
    n = input()
    if n == '0':
        break
    arr.append(n)
print(len(arr))
for i in range(len(arr)):
    if i % 2 == 0:
        print(arr[i])