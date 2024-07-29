def plus_ultra(n):
    if n % 2 == 0:
        if n == 2:
            return 2
        return n + plus_ultra(n - 2)
    else:
        if n == 1:
            return 1
        return n + plus_ultra(n - 2)

n = int(input())
print(plus_ultra(n))