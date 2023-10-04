import math

from src.calculator.figures.figures_parent import FigureParent
from src.calculator.utils.validator import Validator


class Circle(FigureParent):
    @staticmethod
    def calculate_area(radius: float):
        radius = Validator.assert_input_value(radius)
        area = math.pi * radius * radius
        return round(area, 2)
