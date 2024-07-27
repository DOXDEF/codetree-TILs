def various(sent):
    for i in range(len(sent) - 1):
        if sent[i] != sent[i + 1]:
            return True
    return False

s = input()
if various(s):
    print("Yes")
else:
    print("No")