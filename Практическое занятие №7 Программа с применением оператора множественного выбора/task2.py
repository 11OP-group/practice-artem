# Задача 2. Отслеживание заказа
import random

status = input("Введите статус заказа (pending, processing, shipped, delivered, cancelled): ").lower()

match status:
    case "pending":
        status_ru = "В ожидании"
        description = "Ваш заказ принят и ждёт обработки"
        emoji = "⏳"
        time = f"{random.randint(1, 3)}-{random.randint(4, 6)} часов"
        advice = "Скоро мы начнём собирать заказ"
    case "processing":
        status_ru = "В обработке"
        description = "Ваш заказ собирается на складе"
        emoji = "📦"
        time = f"{random.randint(1, 2)}-{random.randint(3, 4)} дня"
        advice = "Ничего делать не нужно"
    case "shipped":
        status_ru = "Отправлено"
        description = "Ваш заказ находится в пути к вам"
        emoji = "✈️"
        time = f"{random.randint(2, 3)}-{random.randint(4, 5)} дней"
        advice = "Следите за уведомлениями о доставке"
    case "delivered":
        status_ru = "Доставлено"
        description = "Ваш заказ доставлен"
        emoji = "✅"
        time = "заказ уже у вас"
        advice = "Не забудьте оставить отзыв"
    case "cancelled":
        status_ru = "Отменено"
        description = "Ваш заказ был отменён"
        emoji = "❌"
        time = "не требуется"
        advice = "Если это ошибка, напишите в поддержку"
    case _:
        print(f'❌ Неизвестный статус "{status}"')
        print("Доступные статусы: pending, processing, shipped, delivered, cancelled")
        exit()

print()
print("╔═══════════════════════════════════════╗")
print("║       📦 СТАТУС ВАШЕГО ЗАКАЗА 📦        ║")
print("╚═══════════════════════════════════════╝")
print()
print(f"Статус: {status_ru} {emoji}")
print(f"Описание: {description}")
print(f"Примерное время: {time}")
print(f"Рекомендация: {advice}")