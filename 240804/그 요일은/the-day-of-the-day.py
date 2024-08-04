m1, d1, m2, d2 = map(int, input().split())
day = input()
arr1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
arr2 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sum1, sum2 = 0, 0
for i in range(m1 - 1):
    sum1 += arr1[i]
sum1 += d1
for i in range(m2 - 1):
    sum2 += arr1[i]
sum2 += d2
cnt_day = 0

cnt_day = (sum2 - sum1) // 7
if (sum2 - sum1) % 7 == arr2.index(day):
    cnt_day += 1
if day == 'Mon':
    cnt_day += 1
print(cnt_day)