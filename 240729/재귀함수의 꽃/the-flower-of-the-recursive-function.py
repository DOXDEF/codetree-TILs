def number(n):
    if n == 0:
        return
    
    print(n, end = " ")
    number(n - 1)
    print(n, end = " ")

n = int(input())
number(n)