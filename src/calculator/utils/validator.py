class Validator:
    @staticmethod
    def assert_input_value(input_value):
        try:
            if input_value or input_value == 0:
                value = float(input_value)

                if 0 <= value:
                    return value
                raise Exception(f"Your value {input_value} must be positive!")

            raise Exception("You enter the empty value!")

        except ValueError:
            raise ValueError(f"Invalid value: {input_value}!")
