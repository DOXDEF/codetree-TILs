def is_369(num):
    num = str(num)
    for i in num:
        if i == '3':
            return True
        elif i == '6':
            return True
        elif i == '9':
            return True

cnt = 0
a, b = map(int, input().split())
for i in range(a, b + 1):
    if i % 3 == 0 or is_369(i):
        cnt += 1
print(cnt)