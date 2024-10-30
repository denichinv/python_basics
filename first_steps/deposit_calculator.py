deposit_sum = float(input())
annual_interest_rate = float(input())
term_months = float(input())

annual_interest = deposit_sum * (annual_interest_rate / 100)

monthly_interest = annual_interest / 12

total_amount = deposit_sum + term_months * monthly_interest

print(total_amount)
