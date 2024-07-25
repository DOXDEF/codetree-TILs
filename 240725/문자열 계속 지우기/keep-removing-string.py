x = input()
y = input()
cnt = 0
while True:
    for i in range(len(x) - (len(y) - 1)):
        x_slice = x[i:len(y) + i]
        if x_slice == y:
            x = x[:i] + x[len(y) + i:]
            cnt += 1
            break
        else:
            pass
    if len(x) <= len(y) and x != y:
        break
    if y not in x:
        break
print(x)