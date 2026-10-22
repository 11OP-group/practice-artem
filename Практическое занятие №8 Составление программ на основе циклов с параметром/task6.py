import random

number = random.randint(1, 10)
answer = False

print(f"Оракул загадал число от 1 до 10... У вас 3 попытки")

for attempt in range(1, 3 + 1):
    guess = int(input(f"Попытка {attempt}: "))
    if guess == number:
        print("Верно!")
        answer = True
        break
    else:
        if guess < number:
            print("Неверно, загаданное число больше")
        else:
            print("Неверно, загаданное число меньше")

if not answer:
    print(f"Вы не угадали. Загаданное число было: {number}")