a, b = map(int, input().split())
print(f"{a // b:.0f}.", end = "")
for i in range(20):
    print(((a % b) * 10) // b, end = "")
    a = ((a % b) * 10) % b