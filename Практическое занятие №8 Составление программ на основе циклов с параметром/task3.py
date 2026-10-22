n = int(input("Введите число, чтобы узнать его знакочередующуюся сумму: "))

total = 0

for i in range(1, n + 1):
    if i % 2 == 1:
        total += i
    else:
        total -= i

print(f"Знакочередующаяся сумма числа {n} = {total}")