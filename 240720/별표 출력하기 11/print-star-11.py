n = int(input())
for i in range(1, n * 2 + 2):
    if i % 2 != 0:
        for j in range(1, n * 2 + 2):
            print("*", end = " ")
        print()
    else:
        for j in range(1, n * 2 + 2):
            if j % 2 != 0:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()