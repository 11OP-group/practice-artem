MIN_SQUARE = 1
MAX_SQUARE = 8

column1, row1 = map(int, input(f"Введите столбец и строку первой клетки ({MIN_SQUARE}-{MAX_SQUARE}) через пробел: ").split())
column2, row2 = map(int, input(f"Введите столбец и строку второй клетки ({MIN_SQUARE}-{MAX_SQUARE}) через пробел: ").split())


if (not MIN_SQUARE <= column1 <= MAX_SQUARE or not MIN_SQUARE <= row1 <= MAX_SQUARE
        or not MIN_SQUARE <= column2 <= MAX_SQUARE or not MIN_SQUARE <= row2 <= MAX_SQUARE):
    print("Данные неверны")
elif (column1 + row1) % 2 == (column2 + row2) % 2:
    print("Цвет клетки совпадает!")
else:
    print("Цвета клетки не совпадают!")