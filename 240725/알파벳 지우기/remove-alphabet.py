x = list(input())
y = list(input())
num = ''
sum_num = 0
for i in x:
    if i >= '0' and i <= '9':
        num += i
sum_num += int(num)
num = ''
for i in y:
    if i >= '0' and i <= '9':
        num += i
sum_num += int(num)
print(sum_num)