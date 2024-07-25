x = list(input())
y = x
print("".join(x))
while True:
    x = x[len(x) - 1:len(x)] + x[0:len(x) - 1]
    print("".join(x))
    if x == y:
        break