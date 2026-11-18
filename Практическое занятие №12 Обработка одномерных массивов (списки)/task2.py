prices = [1500, 500, 2000, 3500, 1000, 4500]

max_price = max(prices)
min_price = min(prices)
sum_price = sum(prices)
mid_price = sum_price / len(prices)

print(f"Самый дорогой товар стоит {max_price}")
print(f"Самый дешевый товар стоит {min_price}")
print(f"Общая стоимость всех товаров: {sum_price}")
print(f"Средняя цена: {mid_price:.2f}")
