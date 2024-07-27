def is_true(x, y):
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
        if y <= 31:
            return True
    elif x == 2:
        if y <= 28:
            return True
    else:
        if y <= 30:
            return True
    return False

a, b = map(int, input().split())
if is_true(a, b):
    print("Yes")
else:
    print("No")