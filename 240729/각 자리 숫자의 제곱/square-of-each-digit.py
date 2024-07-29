def number(n):
    if n < 10:
        return n * n
    return (number(n // 10)) + (n % 10) * (n % 10)

n = int(input())
print(number(n))