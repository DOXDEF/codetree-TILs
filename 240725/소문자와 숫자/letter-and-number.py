n = list(input())
for i in range(len(n)):
    if n[i] >= '0' and n[i] <= '9':
        print(n[i], end = "")
    elif n[i] >= 'a' and n[i] <= 'z':
        print(n[i], end = "")
    elif n[i] >= 'A' and n[i] <= 'Z':
        n[i] = n[i].lower()
        print(n[i], end = "")