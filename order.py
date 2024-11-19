def order_summary(*products, **price):
    if len(products) == 0:
        print("No items ordered.")
        return

    total_price = 0
    print("Grocery List\n")

    for product in products:
        if product not in price:
            print(f"Price for {product} not available.")
        else:
            total_price += float(price[product])
            print(f"{product}: ${price[product]}")

    print(f'\nTotal: ${total_price}')


order_summary("Apple", "Banana", "Cherry", Banana=0.8, Cherry=2.0)