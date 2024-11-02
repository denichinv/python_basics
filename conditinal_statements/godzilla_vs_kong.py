
budget = float(input())
extras_count = int(input())
costume_price_per_extra = float(input())

decor_cost = budget * 0.10

costume_total_cost = extras_count * costume_price_per_extra

if extras_count > 150:
    costume_total_cost = costume_total_cost * 0.90

total_cost = decor_cost + costume_total_cost

if total_cost > budget:
    money_needed = total_cost - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
else:
    money_left = budget - total_cost
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")