#앞에서 2번째 원소와 뒤에서 2번째 원소를 문자 'a'로 대체
n = list(input())
n[1], n[len(n) - 2] = 'a', 'a'
print("".join(n))