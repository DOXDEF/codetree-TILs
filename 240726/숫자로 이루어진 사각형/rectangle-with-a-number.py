def print_num(num):
    x = 1
    for _ in range(num):
        for _ in range(num):
            print(x, end = " ")
            x += 1
            if x == 10:
                x = 1
        print()
n = int(input())
print_num(n)