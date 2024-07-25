arr = list(input())
for _ in range(len(arr) - 1):
    x = int(input())
    if x > len(arr):
        arr.pop(len(arr) - 1)
    else:
        arr.pop(x)
    print("".join(arr))