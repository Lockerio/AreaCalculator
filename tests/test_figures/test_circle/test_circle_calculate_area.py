import pytest

from src.calculator.figures.circle import Circle


positive_results = [([1], 3.14), ([8], 201.06), ([0], 0)]


@pytest.mark.parametrize("input_value, expected_value", positive_results)
def test_calculate_area__positive(input_value, expected_value):
    result_value = Circle.calculate_area(input_value)
    assert result_value == expected_value


value_error_results = ["three", "434fsdf", "1o"]


@pytest.mark.parametrize("input_value", value_error_results)
def test_calculate_area__value_error(input_value):
    with pytest.raises(ValueError):
        Circle.calculate_area(input_value)


error_results = [[1, 2, 3], {1: "1", 2: 2}, -1, "", None, -236, "-12.31"]


@pytest.mark.parametrize("input_value", error_results)
def test_calculate_area__error(input_value):
    with pytest.raises(Exception):
        Circle.calculate_area(input_value)
