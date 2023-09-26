import pytest

from src.calculator.utils.validator import Validator


positive_results = [("1", 1), ("23", 23), ("6789", 6789), ("35.5", 35.5), ("0", 0)]


@pytest.mark.parametrize("input_value, expected_value", positive_results)
def test_assert_input_value__positive(input_value, expected_value):
    result_value = Validator.assert_input_value(input_value)
    assert result_value == expected_value


negative_results = ["three", "434fsdf", "1o"]


@pytest.mark.parametrize("input_value", negative_results)
def test_assert_input_value__negative(input_value):
    with pytest.raises(ValueError):
        Validator.assert_input_value(input_value)


error_results = [[1, 2, 3], {1: "1", 2: 2}, -1, "", None, -236, "-12.31"]


@pytest.mark.parametrize("input_value", error_results)
def test_assert_input_value__value_error(input_value):
    with pytest.raises(Exception):
        Validator.assert_input_value(input_value)
