n = int(input())
arr = list(map(str, input().split()))
cnt = 0
num = 0
line = ''
for i in arr:
    for j in range(len(i)):
        line += i[j]
        cnt += 1
        if cnt == 5:
            print(line)
            line = ''
            num += 1
            cnt = 0
print(num)