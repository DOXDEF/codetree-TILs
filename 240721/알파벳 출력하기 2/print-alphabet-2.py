n = int(input())
alp = 65
for i in range(n):
    for j in range(i):
        print(" ", end = " ")
    for j in range(n - i):
        print(chr(alp), end = " ")
        alp += 1
        if chr(alp) == '[':
            alp = 65
    print()