import math

from src.calculator.figures.figures_parent import FigureParent


class Circle(FigureParent):
    @staticmethod
    def calculate_area(radius):
        if len(radius) == 1 or type(radius) == str:
            radius = Circle.assert_values(radius).pop()
            area = math.pi * radius * radius
            return round(area, 2)
        raise Exception("You enter to many arguments!")
