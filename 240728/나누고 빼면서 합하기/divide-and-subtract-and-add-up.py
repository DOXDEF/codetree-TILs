sum_arr = 0
def plus_ultra(k, arr):
    while True:
        global sum_arr
        sum_arr += arr[k - 1]
        if k == 1:
            break
        elif k % 2 != 0:
            k -= 1
        else:
            k //= 2
n, m = map(int, input().split())
arr = list(map(int, input().split()))
plus_ultra(m, arr)
print(sum_arr)