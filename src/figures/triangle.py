import math

from src.figures.figures_parent import FigureParent


class Triangle(FigureParent):
    @staticmethod
    def calculate_area(a: float, b: float, c: float):
        sides = [a, b, c]
        if Triangle.is_triangle_right(sides[:]):
            hypotenuse = max(sides)
            sides.remove(hypotenuse)
            area = sides.pop() * sides.pop() / 2
            return round(area, 2)

        p = sum(sides) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return round(area, 2)

    @staticmethod
    def is_triangle_right(sides: list[float]):
        hypotenuse = max(sides)
        sides.remove(hypotenuse)
        leg1 = sides.pop()
        leg2 = sides.pop()

        sum_of_squares_of_legs = leg1 * leg1 + leg2 * leg2
        square_of_the_hypotenuse = hypotenuse * hypotenuse

        if sum_of_squares_of_legs == square_of_the_hypotenuse:
            return True
        return False
