a, b = map(int, input().split())
n = input()
digits = []
binary = []

for i in range(len(n)):
    binary.append(int(n[i]))
num = 0

for i in range(len(n)):
    num = num * a + binary[i]

while True:
    if num < b:
        digits.append(num)
        break

    digits.append(num % b)
    num //= b

for digit in digits[::-1]:
    print(digit, end="")