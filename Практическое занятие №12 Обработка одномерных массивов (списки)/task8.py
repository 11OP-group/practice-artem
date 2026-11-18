import random

numbers = [random.randint(1, 100) for i in range(5)]
print(f"Исходный список: {numbers}")

min_index = 0

for i in range(len(numbers)):
    if numbers[i] < numbers[min_index]:
        min_index = i

# print(f"Минимальное значение: {min_index}")
# принт минимального значения. Если надо, то снять комментирование для теста

numbers[0], numbers[min_index] = numbers[min_index], numbers[0]

print(f"Изменённый список: {numbers}")
