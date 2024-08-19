def find_max_N(a):
    max_value = int(a, 2)  # 현재 주어진 이진수를 정수로 변환
    
    # 모든 자리를 하나씩 바꿔가며 가능한 모든 숫자 생성
    for i in range(len(a)):
        if a[i] == '0':
            # 0을 1로 바꿔본다.
            modified_a = a[:i] + '1' + a[i+1:]
        else:
            # 1을 0으로 바꿔본다.
            modified_a = a[:i] + '0' + a[i+1:]
        
        # 수정된 이진수를 정수로 변환
        new_value = int(modified_a, 2)
        
        # 최댓값 갱신
        if new_value > max_value:
            max_value = new_value
    
    return max_value

# 테스트
a = input()
print(find_max_N(a))