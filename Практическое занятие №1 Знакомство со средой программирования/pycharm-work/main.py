import time

while True:
    password = input("Введите пароль: ")

    if password == "42":
        print("Успешный вход")
        break
    else:
        while True:
            print("Ah, ah, ah! You didn't say the magic word!")
            time.sleep(3)
            # В PyCharm/консоли проверка следующего ввода делается через дополнительный инпут
            # Если вам нужно перехватывать ввод прямо во время спама,
            # используем проверку после ввода команды:
            cmd = input("Попробовать снова? (напишите Please!): ")
            if cmd == "Please!":
                break  # Выходит из внутреннего цикла спама и возвращает в начало