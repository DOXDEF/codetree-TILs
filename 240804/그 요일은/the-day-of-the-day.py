m1, d1, m2, d2 = map(int, input().split())
day = input()
arr1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
arr2 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sum1 = sum(arr1[:m1 - 1]) + d1
sum2 = sum(arr1[:m2 - 1]) + d2

cnt_day = 0
for i in range(sum2 - sum1 + 1):
    if arr2[i % 7] == day:
        cnt_day += 1
print(cnt_day)