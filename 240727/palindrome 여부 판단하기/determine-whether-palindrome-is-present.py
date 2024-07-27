def reverse(word):
    new_word = ''
    for i in range(len(word) - 1, -1, -1):
        new_word += word[i]
    return new_word

n = input()
if n == reverse(n):
    print("Yes")
else:
    print("No")