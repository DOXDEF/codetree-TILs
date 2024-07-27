def absolute(num):
    if num % 2 != 0:
        if (num % 100) % 10 != 5:
            if num % 3 != 0 or (num % 3 == 0 and num % 9 == 0):
                return True

cnt = 0
a, b = map(int, input().split())
for i in range(a, b + 1):
    if absolute(i):
        cnt += 1
print(cnt)