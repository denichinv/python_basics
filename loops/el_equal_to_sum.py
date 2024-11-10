n = int(input())
number_sum = 0
biggest_int = float('-inf')
num_list = []

for _ in range(n):
    new_number = int(input())
    if new_number > biggest_int:
        biggest_int = new_number
    number_sum += new_number
    num_list.append(new_number)

remaining_sum = number_sum - biggest_int
if remaining_sum == biggest_int:
    print(f"Yes\nSum = {biggest_int}")
else:
    print(f"No\nDiff = {abs(biggest_int - remaining_sum)}")