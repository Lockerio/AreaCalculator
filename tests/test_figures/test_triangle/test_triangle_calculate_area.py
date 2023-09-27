import pytest

from src.calculator.figures.triangle import Triangle


positive_results = [([3, 4, 5], 6), (["17", 144, 145], 1224), (["11", "60", "51"], 174.64)]


@pytest.mark.parametrize("input_list, expected_values", positive_results)
def test_calculate_area__positive(input_list, expected_values):
    result_values = Triangle.calculate_area(input_list)
    assert result_values == expected_values


error_results = [["", "45", 46], [29, -1, 0], [1, 1, 45], [34, 2, 145], [11, 60, 21],
                 ["-76"], ["-30", 23], [None], [5, 4, None],
                 [{1: 29}, -1, 0], [set("-76")], [["-30"], 23, 11]]


@pytest.mark.parametrize("input_list", error_results)
def test_calculate_area__error(input_list):
    with pytest.raises(Exception):
        Triangle.calculate_area(input_list)
