def jaegyu(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return jaegyu(n // 2) + 1
    else:
        return jaegyu(n * 3 + 1) + 1

n = int(input())
print(jaegyu(n))