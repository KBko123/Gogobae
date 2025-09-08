from datetime import datetime, timedelta

start_date_str = input("날짜와 시간을 입력하세요 (예: 2024-04-19 15): ")

hours_to_add_str = input("몇 시간 후를 계산할까요?: ")

start_datetime = datetime.strptime(start_date_str, "%Y-%m-%d %H")

hours_to_add = int(hours_to_add_str)

# 3. 현재 시각에 입력된 시간을 더하여 미래 시간을 계산합니다.
future_datetime = start_datetime + timedelta(hours=hours_to_add)

# --- 결과 출력 ---
# 계산된 결과를 문제의 예시와 같은 "YYYY년 MM월 DD일 HH시" 형식으로 출력합니다.
result_str = future_datetime.strftime("%Y년 %m월 %d일 %H시")
print(result_str)
