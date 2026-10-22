COUNT_NUMBERS = 10

even = True

print("Введите подряд 10 чисел, чтобы узнать их все ли они чётные, или нет")
for i in range(COUNT_NUMBERS):
    number = int(input())

    if number % 2 != 0: # если остаток от деления на 2 не равен 0, то число не чётное
        even = False

if even:
    print("Все числа чётные!")
else:
    print("Среди этих чисел есть как минимум одно нечётное число")