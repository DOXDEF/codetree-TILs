n = int(input())
cnt = n
for i in range(1, n + 1):
    if i % 2 != 0:
        for j in range((i + 1) // 2):
            print("*", end = " ")
        print()
    else:
        for j in range(cnt):
            print("*", end = " ")
        cnt -= 1
        print()
cnt += 1
for i in range(n, 0, -1):
    if i % 2 != 0:
        for j in range((i + 1) // 2):
            print("*", end = " ")
        print()
    else:
        for j in range(cnt):
            print("*", end = " ")
        cnt += 1
        print()