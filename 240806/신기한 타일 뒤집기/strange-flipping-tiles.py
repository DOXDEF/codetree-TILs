arr = [0] * 200001
point = 100000
n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    if b == 'R':
        for i in range(point, point + int(a)):
            arr[i] = 1
        point += (int(a) - 1)
    else:
        for i in range(point, point - int(a), -1):
            arr[i] = -1
        point -= (int(a) - 1)
print(arr.count(-1), arr.count(1))