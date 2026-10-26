print("Начните ввод оценок")
grade = int(input())
count = 0

while grade >= 1 and grade <= 5:
    if grade == 5:
        count += 1
    grade = int(input())

print(f"Количество оценок «Отлично»: {count}")