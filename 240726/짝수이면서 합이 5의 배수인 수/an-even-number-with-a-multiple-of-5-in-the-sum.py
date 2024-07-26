def is_magic_number(num):
    return num % 2 == 0 and ((num // 10) + (num % 10)) % 5 == 0
n = int(input())
if is_magic_number(n):
    print("Yes")
else:
    print("No")