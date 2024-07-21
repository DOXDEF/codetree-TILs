n = int(input())
alp = 65
for i in range(n):
    for j in range(n):
        print(chr(alp), end = "")
        alp += 1
    print()