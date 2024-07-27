def compare(a, b):
    for i in range(len(a) - len(b) + 1):
        if a[i:len(b) + i] == b:
            return True
    return False

x, y = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
if compare(arr1, arr2):
    print("Yes")
else:
    print("No")