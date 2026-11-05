max = float("-inf")

while True:
        x = int(input("Введите число> "))

        if x == 0:
                break

        elif x > max:
                max = x

print(f"\nМаксимальное число = {max}")