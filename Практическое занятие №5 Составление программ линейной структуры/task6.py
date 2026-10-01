def calculate_distance(x1, y1, x2, y2):
    """
    Вычисляет евклидово расстояние между двумя точками

    Args:
        x1, y1 (float): координаты первой точки
        x2, y2 (float): координаты второй точки

    Returns:
        float: расстояние между точками
    """
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance


def calculate_triangle_area(a, b, c):
    """
    Вычисляет площадь треугольника по формуле Герона

    Args:
        a, b, c (float): длины трех сторон треугольника

    Returns:
        float: площадь треугольника.
    """
    half_perimeter = (a + b + c) / 2
    area = (half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c)) ** 0.5
    return area


# ну типо вводим координаты
x1, y1 = map(float, input("Введите координаты точки A: ").split())
x2, y2 = map(float, input("Введите координаты точки B: ").split())
x3, y3 = map(float, input("Введите координаты точки C: ").split())

# с помощью дефа быстренько всё считаем
side_a = calculate_distance(x1, y1, x2, y2)
side_b = calculate_distance(x2, y2, x3, y3)
side_c = calculate_distance(x3, y3, x1, y1)

# теперь площадь треугольника
triangle_area = calculate_triangle_area(side_a, side_b, side_c)

print(f"Площадь треугольника равна {triangle_area:.2f}")
