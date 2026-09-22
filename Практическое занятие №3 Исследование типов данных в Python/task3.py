# Ввод
num1_str = input("Введите первое число: ")
num2_str = input("Введите первое число: ")

# Преобразование
num1 = int(num1_str)
num2 = int(num2_str)

# Вывод
summa = num1 + num2
print("Сумма: ", summa)

# Если ввести некорректное для int значение, например 'ацуы', то выдаст ошибку "ValueError: invalid literal for int() with base 10: 'ацуы'"