import random

number = random.randint(1, 10)
answer = False

print(f"Оракул загадал число от 1 до 10. У вас 3 попытки, чтобы спасти свою душу...")

for attempt in range(1, 3 + 1):
    print(f"\nПопытка номер {attempt}")
    guess = int(input(f"Введите число: "))
    if guess == number:
        print("Верно! Вы живы!")
        answer = True
        break
    else:
        if guess < number:
            print("Неверно, загаданное число больше")
        else:
            print("Неверно, загаданное число меньше")

if not answer:
    print(f"Ха-ха! Вы не угадали! Оракул загадал число {number}")