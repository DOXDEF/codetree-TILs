n = int(input())
cnt = n
for i in range(1, n + 1):
    for j in range(1, (n + 2) - i):
        print(f"{i} * {j} = {i * j}", end = " ")
        if j == cnt:
            print()
            cnt -= 1
        else:
            print("/", end = " ")