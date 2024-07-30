def rule(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    return rule(n // 3) + rule(n - 1)

n = int(input())
print(rule(n))