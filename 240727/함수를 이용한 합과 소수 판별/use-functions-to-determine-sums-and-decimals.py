def erato(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    if ((num % 10) + (num // 10)) % 2 == 0:
        return True

cnt = 0
a, b = map(int, input().split())
for i in range(a, b + 1):
    if erato(i):
        cnt += 1
print(cnt)