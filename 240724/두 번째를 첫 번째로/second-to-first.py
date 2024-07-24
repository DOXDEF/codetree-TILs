n = list(input())
x = n[1]
y = n[0]
for i in range(len(n)):
    if n[i] == x:
        n[i] = y
print("".join(n))