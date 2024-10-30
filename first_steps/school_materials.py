PEN_PACK = 5.8
MARKER_PACK = 7.2
CLEANING_AGENT_PER_LITRE = 1.2

pack_qty = int(input())
marker_qty = int(input())
agent_litres = int(input())
discount_percent = int(input())

pen_price = pack_qty * PEN_PACK
marker_price = marker_qty * MARKER_PACK
agent_price = CLEANING_AGENT_PER_LITRE * agent_litres

total_price = pen_price + marker_price + agent_price

price_with_discount = total_price - (total_price * discount_percent / 100 )

print(round(price_with_discount,2))