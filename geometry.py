def calculate_rectangle_properties(length: float, width: float) -> dict:
    """Возвращает площадь и периметр прямоугольника в виде словаря."""
    return {
        "area": length * width,
        "perimeter": 2 * (length + width)
    }
