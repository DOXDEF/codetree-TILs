arr = list(map(str, input().split()))
num = ''
sum_num = 0
for i in arr:
    for j in i:
        if j >= '0' and j <= '9':
            num += j
        else:
            break
    sum_num += int(num)
    num = ''
print(sum_num)