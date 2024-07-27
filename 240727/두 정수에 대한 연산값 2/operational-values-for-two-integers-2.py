def plus_ultra(x, y):
    if x > y:
        return x * 2, y + 10
    else:
        return x + 10, y * 2

a, b = map(int, input().split())
a, b = plus_ultra(a, b)
print(a, b)