def gauss(n):
    if n == 1:
        return 1
    return n + gauss(n - 1)

n = int(input())
print(gauss(n))