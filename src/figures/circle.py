import math

from src.figures.figures_parent import FigureParent


class Circle(FigureParent):
    @staticmethod
    def calculate_area(radius: float):
        area = math.pi * radius * radius
        return round(area, 2)
