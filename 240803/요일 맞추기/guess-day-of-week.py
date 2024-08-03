from datetime import datetime

def find_weekday(m1, d1, m2, d2):
    # 기준 날짜와 요일 설정
    base_date = datetime(2011, m1, d1)
    
    # 목표 날짜 설정
    target_date = datetime(2011, m2, d2)
    
    # 두 날짜 사이의 일수 계산
    delta_days = (target_date - base_date).days
    
    # 기준 요일이 월요일(Monday)이므로 0으로 설정 (Monday = 0)
    base_weekday = 0  # Monday
    
    # 목표 날짜의 요일 계산
    target_weekday = (base_weekday + delta_days) % 7
    
    # 요일 배열 (0 = Monday, 6 = Sunday)
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    # 목표 날짜의 요일 출력
    return weekdays[target_weekday]

# 입력 받기
m1, d1, m2, d2 = map(int, input().split())

# 결과 출력
print(find_weekday(m1, d1, m2, d2))