numbers = [10, 20, 30, 40, 50]
search_num = int(input("Введите число: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == search_num:
        print(f"Ваше число есть в списке и имеет индекс {i}")
        found = True
        break

if not found:
    print("Нет такого числа")