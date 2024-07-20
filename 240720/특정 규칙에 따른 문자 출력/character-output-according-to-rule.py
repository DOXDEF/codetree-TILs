n = int(input())
cnt = 1
k = n - 1
for i in range(n * 2 - 1):
    if k >= 0:
        for j in range(k):
            print(" ", end = " ")
    k -= 1
    for j in range(cnt):
        print("@", end = " ")
    print()
    if i < n - 1:
        cnt += 1
    else:
        cnt -= 1