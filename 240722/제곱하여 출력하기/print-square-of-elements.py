n = int(input())
arr = list(map(int, input().split()))
answer = [i * i for i in arr]
for i in answer:
    print(i, end = " ")