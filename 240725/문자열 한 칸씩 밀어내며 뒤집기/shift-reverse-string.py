a, b = map(str, input().split())
a = list(a)
for _ in range(int(b)):
    n = int(input())
    if n == 1:
        a = a[1:] + a[0:1]
        print("".join(a))
    elif n == 2:
        a = a[len(a) - 1:] + a[0:len(a) - 1]
        print("".join(a))
    else:
        a = a[len(a) - 1::-1]
        print("".join(a))