sum = 0
count = 1
DISCOUNT = 0.9

while True:
    price = int(input(f"Введите цену товара {count}> "))

    if price == 0:
        break

    elif price < 0:
        continue

    count += 1
    sum += price

if sum > 1000:
        sum = round(sum * DISCOUNT, 2)
        print("\nСкидка применена! ✨\n")

print(f"Сумма ваших покупок {sum}")