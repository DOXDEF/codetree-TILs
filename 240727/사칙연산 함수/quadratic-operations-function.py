def plus_ultra(num1, num2, alp):
    if alp == '+':
        return num1 + num2
    elif alp == '-':
        return num1 - num2
    elif alp == '*':
        return num1 * num2
    elif alp == '/':
        return num1 // num2
    else:
        return False

a, b, c = map(str, input().split())
a = int(a)
c = int(c)
if plus_ultra(a, c, b):
    print(f"{a} {b} {c} = {plus_ultra(a, c, b)}")
else:
    print(plus_ultra(a, c, b))