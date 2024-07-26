def compare(x, y):
    if x > y:
        for i in range(y + 1, 0, -1):
            if y % i == 0 and x % i == 0:
                print(i)
                break
    else:
        for i in range(x + 1, 0, -1):
            if x % i == 0 and y % i == 0:
                print(i)
                break
a, b = map(int, input().split())
compare(a, b)