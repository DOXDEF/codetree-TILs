n = input()
binary = []
for i in range(len(n)):
    binary.append(int(n[i]))
num = 0

for i in range(len(n)):
    num = num * 2 + binary[i]

print(num)