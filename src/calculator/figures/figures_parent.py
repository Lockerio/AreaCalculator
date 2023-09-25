from src.calculator.utils.validator import Validator


class FigureParent:
    @staticmethod
    def calculate_area():
        pass

    @staticmethod
    def assert_values(raw_values: list):
        if raw_values:
            values = []
            for raw_value in raw_values:
                value = Validator.assert_input_value(raw_value)
                values.append(value)

            if len(values) == 1:
                return values.pop()
            return values

        raise Exception("You enter the empty value!")
