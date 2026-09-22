# 2.1
my_list = [1, 2, 3]
print("Список 1:", my_list)

my_list[0] = 42
print("Список 2:", my_list)
# my_list изменяемый тип данных
# мы можем менять значения элементов и присваивать им новые значения

# 2.2
my_tuple = (1, 2, 3)
print("Кортеж 1:", my_tuple)

# my_tuple[0] = 67
# print("Кортеж 2:", my_tuple)

# При попытке изменить кортеж, выходит ошибка "TypeError: 'tuple' object does not support item assignment"
# Ошибка происходит потому, что tuple (кортеж) - это неизменяемый тип данных


# 2.3
my_string = "cat"
print("Строка 1:", my_string)

# my_string[0] = 'b'
# print("Строка 2:", my_string)

# При попытке изменить строку, выходит ошибка "TypeError: 'str' object does not support item assignment"
# Ошибка происходит потому, что string (строка) - это неизменяемый тип данных