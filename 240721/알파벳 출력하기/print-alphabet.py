n = int(input())
alp = 65
for i in range(1, n + 1):
    for j in range(i):
        print(chr(alp), end = "")
        alp += 1
        if chr(alp) == '[':
            alp = 65
    print()