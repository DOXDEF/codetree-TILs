def func(num):
    sum_val = 0
    for i in range(1, num + 1):
        sum_val += i
    return sum_val // 10
n = int(input())
print(func(n))