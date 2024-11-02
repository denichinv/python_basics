
record_seconds = float(input())
distance_meters = float(input())
time_per_meter = float(input())
base_time = distance_meters * time_per_meter
delays = (distance_meters // 15) * 12.5

total_time = base_time + delays

if total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    difference = total_time - record_seconds
    print(f"No, he failed! He was {difference:.2f} seconds slower.")