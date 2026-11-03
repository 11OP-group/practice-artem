PASSWORD = "admin"

attempts = 3

while True:
    user_password = input("Введите пароль: ")

    if user_password == PASSWORD:
        print("Добро пожаловать, сэр!")
        break

    attempts -= 1

    if attempts == 0:
        print("Попытки закончились! Попробуйте позже")
        break

    print(f"Неверный пароль, попыток осталось: {attempts}\n")