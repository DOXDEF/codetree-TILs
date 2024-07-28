n, m = map(int, input().split())
arr = list(map(int, input().split()))

def plus_ultra(x, y):
    global arr
    sum_arr = 0
    for i in range(x - 1, y):
        sum_arr += arr[i]
    print(sum_arr)
    

for _ in range(m):
    a, b = map(int, input().split())
    plus_ultra(a, b)