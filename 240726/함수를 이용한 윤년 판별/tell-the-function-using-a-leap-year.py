def Yoon(num):
    if num % 4 != 0:
        return False
    elif num % 100 == 0 and num % 400 != 0:
        return False
    else:
        return True

n = int(input())
if Yoon(n):
    print("true")
else:
    print("false")