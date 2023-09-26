import pytest

from src.calculator.figures.figures_parent import FigureParent


positive_results = [([1], 1), (["1", 2, 0], [1, 2, 0]), (["10"], 10)]


@pytest.mark.parametrize("input_list, expected_values", positive_results)
def test_assert_values__positive(input_list, expected_values):
    result_values = FigureParent.assert_values(input_list)
    assert result_values == expected_values


negative_results = [[""], ["", "45", 46], [29, -1, 0],
                    ["-76"], ["-30", 23], [None], [5, 4, None],
                    [{1: 29}, -1, 0], [set("-76")], [["-30"], 23]]


@pytest.mark.parametrize("input_list", negative_results)
def test_assert_values__negative(input_list):
    with pytest.raises(Exception):
        FigureParent.assert_values(input_list)


error_results = [["asd"], ["q", "4ada5", 46, 52], [4, "three"]]


@pytest.mark.parametrize("input_list", error_results)
def test_assert_values__value_error(input_list):
    with pytest.raises(ValueError):
        FigureParent.assert_values(input_list)
