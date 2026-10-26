word = input().lower()
count = 0

while word != "стоп" and word != "хватит" and word != "достаточно":
    count += 1
    word = input().lower()

print(f"Количество введённых слов: {count}")