
from geometry import calculate_area

def test_calculate_area():
    assert calculate_area(5, 10) == 50
    assert calculate_area(0, 10) == 0
    assert calculate_area(3.5, 2) == 7.0