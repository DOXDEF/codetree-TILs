def fact_check(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    
    return n * fact_check(n - 1)

n = int(input())
print(fact_check(n))