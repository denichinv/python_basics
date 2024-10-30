x = int(input())
z = int(input())
y = int(input())
percent = int(input())/ 100

area = x * z * y

area_in_litres =  area / 1000
liters_to_fill = area_in_litres * (1- percent)
print(liters_to_fill)