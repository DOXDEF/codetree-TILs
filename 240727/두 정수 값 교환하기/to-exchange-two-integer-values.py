def swap(x, y):
    x, y = y, x
    return x, y

a, b = map(int, input().split())
a, b = swap(a, b)
print(a, b)