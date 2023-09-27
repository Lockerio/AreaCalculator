import math

from src.calculator.figures.figures_parent import FigureParent
from src.calculator.utils.validator import Validator


class Circle(FigureParent):
    @staticmethod
    def calculate_area(radius):
        if len(radius) == 1 or type(radius) == str:
            radius = Validator.assert_input_value(radius)
            area = math.pi * radius * radius
            print(area)
            return round(area, 2)
        raise Exception("You enter to many arguments!")
