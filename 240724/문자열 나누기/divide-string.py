n = int(input())
arr = list(map(str, input().split()))
cnt = 0
num = 0
for i in arr:
    for j in range(len(i)):
        print(i[j], end = "")
        cnt += 1
        if cnt == 5:
            print()
            num += 1
            cnt = 0