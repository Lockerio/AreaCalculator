import pytest

from src.calculator.figures.triangle import Triangle


positive_results = [([3, 4, 5], True), (["17", 144, 145], True), ([11, 60, 61], True)]


@pytest.mark.parametrize("input_list, expected_values", positive_results)
def test_is_triangle_right__positive(input_list, expected_values):
    result_values = Triangle.is_triangle_right(input_list)
    assert result_values == expected_values


negative_results = [([1, 1, 45], False), ([34, 2, 145], False), ([11, 60, 21], False)]


@pytest.mark.parametrize("input_list, expected_values", negative_results)
def test_is_triangle_right__negative(input_list, expected_values):
    result_values = Triangle.is_triangle_right(input_list)
    assert result_values == expected_values


error_results = [["", "45", 46], [29, -1, 0],
                 ["-76"], ["-30", 23], [None], [5, 4, None],
                 [{1: 29}, -1, 0], [set("-76")], [["-30"], 23, 11]]


@pytest.mark.parametrize("input_list", error_results)
def test_is_triangle_right__error(input_list):
    with pytest.raises(Exception):
        Triangle.is_triangle_right(input_list)

