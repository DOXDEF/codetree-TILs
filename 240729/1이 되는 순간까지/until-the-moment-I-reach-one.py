cnt = 0

def div(n):
    global cnt
    if n == 1:
        return 0
    
    if n % 2 == 0:
        cnt += 1
        return div(n // 2)
    else:
        cnt += 1
        return div(n // 3)

n = int(input())
div(n)
print(cnt)