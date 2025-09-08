from datetime import datetime, timedelta

start_date_str = input("날짜와 시간을 입력하세요 (예: 2024-04-19 15): ")

hours_to_add_str = input("몇 시간 후를 계산할까요?: ")

start_datetime = datetime.strptime(start_date_str, "%Y-%m-%d %H")

hours_to_add = int(hours_to_add_str)

future_datetime = start_datetime + timedelta(hours=hours_to_add)

result_str = future_datetime.strftime("%Y년 %m월 %d일 %H시")
print(result_str)
