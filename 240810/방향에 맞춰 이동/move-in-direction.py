dw, ds, dn, de = [-1, 0], [0, -1], [0, 1], [1, 0]
x, y = 0, 0
n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    if a == 'W':
        x, y = x + (dw[0] * int(b)), y + (dw[1] * int(b))
    elif a == 'S':
        x, y = x + (ds[0] * int(b)), y + (ds[1] * int(b))
    elif a == 'N':
        x, y = x + (dn[0] * int(b)), y + (dn[1] * int(b))
    else:
        x, y = x + (de[0] * int(b)), y + (de[1] * int(b))
print(x, y)