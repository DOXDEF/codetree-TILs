def plus_ultra(n):
    if n < 10:
        return n
    return plus_ultra(n // 10) + (n % 10)

a, b, c = map(int, input().split())
num = 0
num = a * b * c
print(plus_ultra(num))