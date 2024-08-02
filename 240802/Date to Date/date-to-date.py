m1, d1, m2, d2 = map(int, input().split())
arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum1, sum2 = 0, 0
for i in range(m1):
    sum1 += arr[i]
sum1 += d1
for i in range(m2):
    sum2 += arr[i]
sum2 += d2
print(sum2 - sum1)