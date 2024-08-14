n = int(input())
arr = list(map(int, input().split()))
min_dist = 9999999
for i in range(n):
    dist = 0
    for j in range(n):
        dist += arr[j] * abs(i - j)
    if dist < min_dist:
        min_dist = dist
print(min_dist)