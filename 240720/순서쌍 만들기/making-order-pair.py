n = int(input())
cnt = n
for i in range(n):
    for j in range(n, 0, -1):
        print(f"({cnt},{j})", end = " ")
    print()
    cnt -= 1