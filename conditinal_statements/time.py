hours = int(input())
minutes = int(input())

additional_time = 15

total_time_in_minutes = (hours * 60) + minutes + additional_time

new_hour = total_time_in_minutes // 60
new_minutes = total_time_in_minutes % 60

if new_hour == 24:
    new_hour = 0

if new_minutes < 10:
    print(f"{new_hour}:0{new_minutes}")
else:
    print(f"{new_hour}:{new_minutes}")

