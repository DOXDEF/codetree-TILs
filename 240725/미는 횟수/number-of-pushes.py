a = input()
b = input()
n = 0
while a != b:
    a = a[len(a) - 1:] + a[0:len(a) - 1]
    n += 1
    if n == len(a):
        n = -1
        break
if n != -1:
    print(n)
else:
    print(-1)