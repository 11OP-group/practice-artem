while True:
    rating_text = input("Введите рейтинг продукта (от 1 до 10): ").strip()

    if rating_text.isdigit():
        rating = int(rating_text)

        match rating:
            case 9 | 10:
                description = "Отличный"
                emoji = "🤩"
                recommendation = "Рекомендую"
            case 7 | 8:
                description = "Хороший"
                emoji = "😊"
                recommendation = "Рекомендую"
            case 4 | 5 | 6:
                description = "Средний"
                emoji = "😐"
                recommendation = "Можно попробовать"
            case 1 | 2 | 3:
                description = "Плохой"
                emoji = "😞"
                recommendation = "Не рекомендую"
            case _:
                print("❌ Ошибка: рейтинг должен быть целым числом от 1 до 10")
                continue

        print("=" * 36)
        print(f"⭐ Рейтинг: {rating}/10")
        print(f"{emoji} Оценка: {description}")
        print(f"💬 Рекомендация: {recommendation}")
        print("=" * 36)
        break
    else:
        print("❌ Ошибка: рейтинг должен быть целым числом от 1 до 10")