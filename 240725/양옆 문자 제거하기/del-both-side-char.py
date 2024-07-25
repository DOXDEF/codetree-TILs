n = list(input())
n.pop(1)
n.pop(len(n) - 2)
print("".join(n))