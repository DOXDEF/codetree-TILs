def hund(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    return (hund(n - 1) * hund(n - 2)) % 100

n = int(input())
print(hund(n))