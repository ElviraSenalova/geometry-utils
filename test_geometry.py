from geometry import calculate_rectangle_properties

def test_calculate_rectangle_properties():
    result = calculate_rectangle_properties(5, 10)
    assert result["area"] == 50
    assert result["perimeter"] == 30
