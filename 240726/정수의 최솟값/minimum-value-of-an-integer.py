def min_num(a = 0, b = 0, c = 0):
    if a <= b:
        if a <= c:
            return a
        else:
            return c
    else:
        if b <= c:
            return b
        else:
            return c
x, y, z = map(int, input().split())
print(min_num(x, y, z))