n = int(input()) 
num = 0
for _ in range(n):
    k = int(input())
    num += k
num = str(num)
print(num[1:] + num[:1])