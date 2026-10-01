EXCHANGE_RATE = 95.50  # курс доллара к рублю


def convert_exchange_rate(amount_usd):
    """
    Переводит сумму из долларов в рубли по курсу

    Args:
        amount_usd (float): сумма в долларах

    Returns:
        float: сумма в рублях
    """
    return amount_usd * EXCHANGE_RATE


# вводим сумма
text = input("Введите сумму в долларах: ")
amount_usd = float(text)

# считаем
amount_rub = convert_exchange_rate(amount_usd)

print(f"{amount_usd:.2f} = {amount_rub:.2f} руб.")
