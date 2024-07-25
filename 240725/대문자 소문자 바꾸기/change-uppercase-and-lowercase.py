n = list(input())
for i in range(len(n)):
    if n[i] >= 'a' and n[i] <= 'z':
        n[i] = n[i].upper()
    else:
        n[i] = n[i].lower()
print("".join(n))