# -*- coding: utf-8 -*-

from typing import List


def get_average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)


# b - intercept, m - coefficient
# assumption: len(xs) == len(ys)
def get_intercept(xs: List[float], ys: List[float], coefficient: float) -> float:
    return get_average(ys) - coefficient * get_average(xs)


# assumption: len(xs) == len(ys)
def get_sum_of_x_y_products(xs: List[float], ys: List[float]) -> float:
    return sum([x * y for (x, y) in zip(xs, ys)])


# assumption: len(xs) == len(ys)
def get_product_of_x_y_sums(xs: List[float], ys: List[float]) -> float:
    return sum(xs) * sum(ys)


def get_sum_of_x_squares(xs: List[float]) -> float:
    return sum([x * x for x in xs])


# b - intercept, m - coefficient
# assumption: len(xs) == len(ys)
def get_coefficient(xs: List[float], ys: List[float]) -> float:
    n: int = len(xs)
    numerator_part1: float = get_sum_of_x_y_products(xs, ys)
    numerator_part2: float = get_product_of_x_y_sums(xs, ys) / n
    denominator_part1: float = get_sum_of_x_squares(xs)
    denominator_part2: float = (sum(xs) ** 2) / n
    numerator: float = numerator_part1 - numerator_part2
    denominator: float = denominator_part1 - denominator_part2
    return numerator / denominator


def print_linear_regression_formula(xs: List[float], ys: List[float]) -> None:
    coefficient: float = get_coefficient(xs, ys)
    intercept: float = get_intercept(xs, ys, coefficient)
    print("\nFormula for line of best fit (y = b + mx) is:")
    print("y = {0} + {1}x".format(intercept, coefficient))


def get_xy_coordinates_from_user(
    min_incl: float = -1e3, max_incl: float = 1e3
) -> List[float]:
    data_collected: bool = False
    point: List[float] = []
    while not data_collected:
        input_str: str = input(
            "Enter {0} coordinate (integer from {1} and {2}): ".format(
                "x" if len(point) == 0 else "y", min_incl, max_incl
            )
        )
        try:
            value: float = float(input_str)
            if not (min_incl <= value <= max_incl):
                print("Number outside of range.")
                raise ValueError
            point.append(value)
        except ValueError:
            print("Incorrect input, try again.")
        if len(point) == 2:
            data_collected = True
    return point


# returns List of points, e.g. [[1,2], [2,3], [4,5]]
def get_points_from_user() -> List[List[float]]:
    data_collected: bool = False
    points: List[List[float]] = []
    print("Beginning data acquisition.")
    print("Enter the coordinates of at least two different points.")
    print("Enter no more than 10 points.")
    while not data_collected:
        print("")
        points.append(get_xy_coordinates_from_user())
        data_collected = len(points) >= 10
        if not data_collected:
            data_collected = input(
                "\nAnother point [Y/n or anything else]? "
            ).strip() not in ["y", "Y", ""]
        else:
            print("Collected 10 data points.")
    print("End of data acquisition.")
    return points


# points, e.g. [[1,2], [2,3], [4,5]]
def get_unique_points(points: List[List[float]]) -> List[List[float]]:
    unique_points: List[List[float]] = []
    for point in points:
        if point not in unique_points:
            unique_points.append(point)
    return unique_points


# points, e.g. [[1,2], [2,3], [4,5]]
def are_points_ok(points: List[List[float]]) -> bool:
    return len(get_unique_points(points)) >= 2


# points, e.g. [[1,2], [2,3], [4,5]]
# returns, e.g. [[1, 2, 4], [2, 3, 5]]
def get_xs_ys_from_points(points: List[List[float]]) -> List[List[float]]:
    xs: List[float] = []
    ys: List[float] = []
    for [x, y] in points:
        xs.append(x)
        ys.append(y)
    return [xs, ys]


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program that asks user to enter points coordinates.")
    print("Next it calculates formula for line of best fit for the points.")
    print("The formula for linear regression is printed on the screen.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()
    points = get_points_from_user()
    if not are_points_ok(points):
        print("\nIncorrect input. Required coordinates for >= two different points.")
        print("Found {0} unique point(s).".format(len(get_unique_points(points))))
        print("Terminating the program.")
    else:
        try:
            xs, ys = get_xs_ys_from_points(points)
            print_linear_regression_formula(xs, ys)
        except ZeroDivisionError:
            print("Cannot compute coefficient.")
            print("Probable cause: points form vertical line on a graph.")
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
