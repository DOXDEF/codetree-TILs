def compare(x, y):
    a = x
    b = y
    if x > y:
        while x % y != 0:
            x += a
        print(x)
    else:
        while y % x != 0:
            y += b
        print(y)
n, m = map(int, input().split())
compare(n, m)