# цены на напитки
PRICE_COFFEE = 120
PRICE_TEA = 80
PRICE_JUICE = 100
PRICE_WATER = 50
PRICE_LEMONADE = 90

# размер скидок
DISCOUNT_STUDENT = 20
DISCOUNT_SALE10 = 10

print("☕ Меню кафе:")
print(f"1. Кофе ☕ - {PRICE_COFFEE} руб")
print(f"2. Чай 🍵 - {PRICE_TEA} руб")
print(f"3. Сок 🧃 - {PRICE_JUICE} руб")
print(f"4. Вода 💧 - {PRICE_WATER} руб")
print(f"5. Лимонад 🥤 - {PRICE_LEMONADE} руб")
print()

drink = input("Введите номер напитка (1-5) или его название: ").strip().lower()

# выбор напитка
match drink:
    case "1" | "кофе" | "coffee":
        name = "Кофе"
        emoji = "☕"
        price = PRICE_COFFEE
    case "2" | "чай" | "tea":
        name = "Чай"
        emoji = "🍵"
        price = PRICE_TEA
    case "3" | "сок" | "juice":
        name = "Сок"
        emoji = "🧃"
        price = PRICE_JUICE
    case "4" | "вода" | "water":
        name = "Вода"
        emoji = "💧"
        price = PRICE_WATER
    case "5" | "лимонад" | "lemonade":
        name = "Лимонад"
        emoji = "🥤"
        price = PRICE_LEMONADE
    case _:
        print(f'❌ Напитка "{drink}" нет в меню')
        exit()

quantity_text = input("Введите количество порций: ").strip()

# проверяем, что ввели целое число
match quantity_text.isdigit():
    case True:
        quantity = int(quantity_text)
    case _:
        print(f'❌ "{quantity_text}" - это не количество порций')
        exit()

# количество не может быть нулём
match quantity:
    case 0:
        print("❌ Нужно заказать хотя бы одну порцию")
        exit()

code = input("Введите промокод (если его нет, просто нажмите Enter): ").strip().upper()

# проверка промокода
match code:
    case "":
        discount_percent = 0
    case "STUDENT":
        discount_percent = DISCOUNT_STUDENT
    case "SALE10":
        discount_percent = DISCOUNT_SALE10
    case _:
        print(f'⚠️ Промокод "{code}" не существует, напиток будет продан по полной цене')
        discount_percent = 0

# склонение слова "порция"
match quantity % 100:
    case 11 | 12 | 13 | 14:
        word = "порций"
    case _:
        match quantity % 10:
            case 1:
                word = "порция"
            case 2 | 3 | 4:
                word = "порции"
            case _:
                word = "порций"

total = price * quantity
discount = total * discount_percent // 100
final_sum = total - discount

print()
print("╔════════════════════════════╗")
print("║     ☕ КВИТАНЦИЯ КАФЕ ☕     ║")
print("╚════════════════════════════╝")
print()
print(f"Товар: {name} {emoji}")
print(f"Цена за порцию: {price} руб")
print(f"Количество: {quantity} {word}")
print(f"Сумма: {total} руб")
print()

# скидку показываем, только если она есть
match discount_percent:
    case 0:
        pass
    case _:
        print(f'Скидка "{code}" ({discount_percent}%): -{discount} руб')

print("══════════════════════════════")
print(f"💰 К ОПЛАТЕ: {final_sum} руб")
print("══════════════════════════════")