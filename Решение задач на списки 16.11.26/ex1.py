prices = [100, 50, 200, 150]
print(f"Макс. цена: {max(prices)} | Мин. цена: {min(prices)}")
print(f'Ср. цена: {sum(prices)/len(prices)}')
print(*prices, sep = ', ')