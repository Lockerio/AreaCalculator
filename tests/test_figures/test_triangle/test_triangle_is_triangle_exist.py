import pytest

from src.calculator.figures.triangle import Triangle


positive_results = [([1, 1, 1], True), ([3, 4, 5], True), ([24, 18, 23], True)]


@pytest.mark.parametrize("input_list, expected_values", positive_results)
def test_is_triangle_exist__positive(input_list, expected_values):
    result_values = Triangle.is_triangle_exist(input_list)
    assert result_values == expected_values


negative_results = [([0, 0, 0], False), ([52, 4, 78], False), ([23, 18, 1], False)]


@pytest.mark.parametrize("input_list, expected_values", negative_results)
def test_is_triangle_exist__negative(input_list, expected_values):
    result_values = Triangle.is_triangle_exist(input_list)
    assert result_values == expected_values


error_results = [[""], ["", "45", 46],
                 ["-76"], ["-30", 23], [None], [5, 4, None],
                 [{1: 29}, -1, 0], [set("-76")], [["-30"], 23]]


@pytest.mark.parametrize("input_list", error_results)
def test_is_triangle_exist__error(input_list):
    with pytest.raises(Exception):
        Triangle.is_triangle_exist(input_list)
