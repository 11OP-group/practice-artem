print("Начните ввод чисел, которые делятся на 7")
num = int(input())
result = ""

while num % 7 == 0:
    result += str(num) + ", "
    num = int(input())

print(f"Числа, делящиеся на 7: {result}")