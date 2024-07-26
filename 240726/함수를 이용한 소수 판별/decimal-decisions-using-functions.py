def is_dec(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

a, b = map(int, input().split())
if b == 1:
    print(1)
sum_dec = 0
for i in range(a, b + 1):
    if is_dec(i):
        sum_dec += i
print(sum_dec)