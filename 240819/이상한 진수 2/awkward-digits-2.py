def find_max_N(a):
    possible_values = []
    
    # 모든 자리를 하나씩 바꿔가며 가능한 모든 숫자 생성
    for i in range(len(a)):
        if a[i] == '0':
            # 0을 1로 바꿔본다.
            modified_a = a[:i] + '1' + a[i+1:]
        else:
            # 1을 0으로 바꿔본다.
            modified_a = a[:i] + '0' + a[i+1:]
        
        # 수정된 이진수를 정수로 변환하여 리스트에 추가
        possible_values.append(int(modified_a, 2))
    
    # 가능한 값들 중 최댓값을 반환
    return max(possible_values)

# 테스트
a = input()
print(find_max_N(a))