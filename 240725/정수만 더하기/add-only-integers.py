n = list(input())
sum_int = 0
for i in range(len(n)):
    if n[i] >= '0' and n[i] <= '9':
        sum_int += int(n[i])
print(sum_int)