def parrot(n):
    if n == 0:
        return
    parrot(n - 1)
    print("HelloWorld")

n = int(input())
parrot(n)