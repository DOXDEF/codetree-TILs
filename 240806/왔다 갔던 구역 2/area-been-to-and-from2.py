arr = [0] * 2001
point = 1000
n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    if b == 'R':
        for i in range(int(a)):
            arr[point] += 1
            point += 1
    else:
        for i in range(int(a)):
            point -= 1
            arr[point] += 1
print(len(arr) - (arr.count(0) + arr.count(1)))