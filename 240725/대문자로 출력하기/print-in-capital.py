n = list(input())
for i in range(len(n)):
    if n[i] >= 'a' and n[i] <= 'z':
        n[i] = n[i].upper()
        print(n[i], end = "")
    elif n[i] >= 'A' and n[i] <= 'Z':
        print(n[i], end = "")