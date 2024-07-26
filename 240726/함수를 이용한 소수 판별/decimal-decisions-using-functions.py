def is_dec(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

a, b = map(int, input().split())
sum_dec = 0
if b == 1:
    print(0)
else:
    for i in range(a, b + 1):
        if is_dec(i):
            sum_dec += i
    print(sum_dec)