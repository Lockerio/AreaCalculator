import math

from src.calculator.figures.figures_parent import FigureParent


class Circle(FigureParent):
    @staticmethod
    def calculate_area(radius):
        radius = Circle.assert_values(radius)
        area = math.pi * radius * radius
        return round(area, 2)
