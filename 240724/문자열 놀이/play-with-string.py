a, b = map(str, input().split())
a = list(a)
for _ in range(int(b)):
    x, y, z = map(str, input().split())
    if x == '1':
        a[int(y) - 1], a[int(z) - 1] = a[int(z) - 1], a[int(y) - 1]
        print("".join(a))
    else:
        for i in range(len(a)):
            if a[i] == y:
                a[i] = z              
        print("".join(a))