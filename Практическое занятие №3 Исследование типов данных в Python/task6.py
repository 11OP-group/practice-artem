# 1. Сбор данных от пользователя
name = input("Ваше имя: ")
age_str = input("Ваш возраст: ")
subjects_str = input("Любимые предметы (через запятую): ")

# 2. Преобразование типов
age = int(age_str)

# 3. Создание словаря
student = {
    "name": name,
    "age": age,
    "subjects": subjects_str
}

# 4. Красивый вывод анкеты
print("=" * 30)
print("АНКЕТА СТУДЕНТА")
print("=" * 30)

print("Имя:", student['name'])
print("Возраст:", student['age'])
print("Любимые предметы:", student['subjects'])

print("=" * 30)