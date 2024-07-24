a = list(input())
x = a[0]
y = a[1]
for i in range(len(a)):
    if a[i] == x:
        a[i] = y
    elif a[i] == y:
        a[i] = x
print("".join(a))