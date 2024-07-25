arr = list(map(str, input().split()))
num = ''
sum_num = 0
for i in arr:
    for j in i:
        if j >= '0' and j <= '9':
            num += j
        else:
            sum_num += int(num)
            num = ''
            break
print(sum_num)