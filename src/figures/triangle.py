import math

from src.figures.figures_parent import FigureParent


class Triangle(FigureParent):
    def calculate_area(self, a: float, b: float, c: float):
        sides = [a, b, c]
        if self.is_triangle_right(sides):
            hypotenuse = max(sides)
            sides.remove(hypotenuse)
            area = sides.pop() * sides.pop() / 2
            return round(area, 2)

        p = sum(sides) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return round(area, 2)

    def is_triangle_right(self, sides: list[float]):
        hypotenuse = max(sides)
        sides.remove(hypotenuse)
        leg1 = sides.pop()
        leg2 = sides.pop()
        return self.check_triangle_by_Pythagorean_theorem(leg1, leg2, hypotenuse)

    @staticmethod
    def check_triangle_by_Pythagorean_theorem(a: float, b: float, c: float):
        sum_of_squares_of_legs = a * a + b * b
        square_of_the_hypotenuse = c * c

        if sum_of_squares_of_legs == square_of_the_hypotenuse:
            return True
        return False
