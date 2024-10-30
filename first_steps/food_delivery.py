CHICKEN_MENU,FISH_MENU,VEG_MENU = 10.35,12.4,8.15
DELIVERY_COST = 2.5

chicken_menu_qty =  int(input()) * CHICKEN_MENU
fish_menu_qty =  int(input()) * FISH_MENU
veg_menu_qty =  int(input()) * VEG_MENU

order_price = chicken_menu_qty + fish_menu_qty + veg_menu_qty

desert_price = order_price * 0.2

total_price = desert_price + order_price + DELIVERY_COST

print(total_price)

