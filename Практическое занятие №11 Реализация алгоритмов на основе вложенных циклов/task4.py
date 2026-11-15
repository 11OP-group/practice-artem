n = int(input("Введите натуральное число: "))

last = n % 10

count_3 = 0
count_last = 0
count_even = 0
sum_big5 = 0
prod_big7 = 1
count_0_5 = 0

while n > 0:
    number = n % 10

    if number == 3:
        count_3 += 1
    if number == last:
        count_last += 1
    if number % 2 == 0:
        count_even += 1
    if number > 5:
        sum_big5 += number
    if number > 7:
        prod_big7 *= number
    if number == 0 or number == 5:
        count_0_5 += 1
    n = n // 10

print(f"Количество цифр 3: {count_3}")
print(f"Сколько раз встречается последняя цифра: {count_last}")
print(f"Количество чётных цифр: {count_even}")
print(f"Сумма цифр больше 5: {sum_big5}")
print(f"Произведение цифр больше 7: {prod_big7}")
print(f"Количество цифр 0 и 5: {count_0_5}")

# Эта задача 1 в 1 уже была в 9 практике кстати)