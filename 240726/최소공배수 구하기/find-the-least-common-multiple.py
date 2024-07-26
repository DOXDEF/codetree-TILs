def compare(x, y):
    num = 2
    if x > y:
        while x % y != 0:
            x *= num
            num += 1
        print(x)
    else:
        while y % x != 0:
            y *= num
            num += 1
        print(y)
n, m = map(int, input().split())
compare(n, m)