arr = [0] * 2001
point = 1000
n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    if b == 'R':
        for i in range(point, point + int(a)):
            arr[i] += 1
        point += int(a)
    else:
        for i in range(point, point - int(a), -1):
            arr[i] += 1
        point -= int(a)
print(len(arr) - (arr.count(0) + arr.count(1)))