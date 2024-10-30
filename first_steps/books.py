
book_pages = int(input())
pages_for_hour = int(input())
days_to_finish = int(input())

total_time_needed = (book_pages / pages_for_hour)/days_to_finish
print(round(total_time_needed))