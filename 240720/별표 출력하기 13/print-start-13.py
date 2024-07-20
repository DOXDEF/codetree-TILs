n = int(input())
cnt = n
for i in range(1, n * 2 + 1):
    if i % 2 == 0:
        for j in range(i // 2):
            print("*", end = " ")
        print()
    else:
        for j in range(cnt):
            print("*", end = " ")
        print()
        cnt -= 1