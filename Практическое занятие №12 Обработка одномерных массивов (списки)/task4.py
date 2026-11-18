import random

marks = [random.randint(2, 5) for i in range(10)]

# print(marks)
# принт исходного списка. Если надо, то снять комментирование для теста

count_fives = 0
count_twos = 0

for mark in marks:
    if mark == 5:
        count_fives += 1
    elif mark == 2:
        count_twos += 1

print(f"Всего пятёрок: {count_fives}")
print(f"Всего двоек: {count_twos}")