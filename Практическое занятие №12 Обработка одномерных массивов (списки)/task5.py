data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_three = data[:3]
last_three = data[-3:]
inverted_list = data[::-1]
odd_elements = data[1::2]

print(f"Первая тройка: {first_three}")
print(f"Последняя тройка: {last_three}")
print(f"Список в обратном порятке {inverted_list}")
print(f"Нечетные элементы {odd_elements}")