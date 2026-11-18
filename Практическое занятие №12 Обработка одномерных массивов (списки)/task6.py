chars = list(input("Введите слово: ").lower())

inverted_chars = chars[::-1]

if chars == inverted_chars:
    print("Это палиндром")
else:
    print("Не палиндром")