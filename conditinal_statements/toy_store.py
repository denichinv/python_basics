

puzzle = 2.60
talking_doll = 3
teddy_bear = 4.10
minion =8.20
truck = 2

trip_price = float(input())
order_puzzle = int(input())
order_doll = int(input())
order_bear = int(input())
order_minion = int(input())
order_truck = int(input())

total_order_price = (puzzle * order_puzzle) + (talking_doll * order_doll) + (teddy_bear * order_bear) + (minion * order_minion ) + (truck * order_truck)
qty_toys_ordered  = order_puzzle + order_doll + order_bear + order_minion + order_truck

if qty_toys_ordered >= 50:
    total_order_price *= 0.75

total_order_price *= 0.9
if total_order_price >= trip_price:
    print(f"Yes! {total_order_price - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - total_order_price:.2f} lv needed.")

