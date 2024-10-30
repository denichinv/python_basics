
NYLON_PER_SQM =  1.5
PAINT_PER_LITRE = 14.5
PAINT_THINNER_PER_LITRE = 5
BAGS = 0.4

nylon_needed = ( (int(input()) + 2) * NYLON_PER_SQM)
paint_needed = ((int(input())*1.1) * PAINT_PER_LITRE)
paint_thinner_needed = int(input()) * PAINT_THINNER_PER_LITRE

total_material_price = nylon_needed + paint_needed + paint_thinner_needed +BAGS


workers_hours = int(input()) *(total_material_price * 0.3)
total_price = workers_hours + total_material_price

print(total_price)


