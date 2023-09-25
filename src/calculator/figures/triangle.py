import math

from src.calculator.figures.figures_parent import FigureParent


class Triangle(FigureParent):
    @staticmethod
    def calculate_area(sides: list):
        sides = Triangle.assert_values(sides[:])
        if Triangle.is_triangle_exist(sides[:]):
            if Triangle.is_triangle_right(sides[:]):
                hypotenuse = max(sides)
                sides.remove(hypotenuse)
                area = sides.pop() * sides.pop() / 2
                return round(area, 2)

            p = sum(sides) / 2
            area = math.sqrt(p * (p - sides.pop()) * (p - sides.pop()) * (p - sides.pop()))
            return round(area, 2)
        raise Exception("Such triangle does not exist!")

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

    @staticmethod
    def is_triangle_exist(sides: list[float]):
        max_side = max(sides)
        sides.remove(max_side)
        if sides.pop() + sides.pop() > max_side:
            return True
        return False
