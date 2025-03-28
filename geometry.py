# geometry.py

def calculate_rectangle_properties(length: float, width: float) -> dict:
    """
    Как повар готовит блюдо, эта функция формирует "рецепт" прямоугольника,
    возвращая его площадь и периметр.
    """
    return {
        "area": length * width,  # Площадь - основа блюда
        "perimeter": 2 * (length + width)  # Периметр - его границы, словно тарелка
    }
