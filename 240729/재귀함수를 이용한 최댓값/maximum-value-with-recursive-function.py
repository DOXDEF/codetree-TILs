num_max = 0
def maxi(n, arr):
    global num_max
    if n == 0:
        return num_max + arr[0]
    maxi(n - 1, arr)
    if num_max < arr[n - 1]:
        num_max = arr[n - 1]

n = int(input())
arr = list(map(int, input().split()))
maxi(n, arr)
print(num_max)