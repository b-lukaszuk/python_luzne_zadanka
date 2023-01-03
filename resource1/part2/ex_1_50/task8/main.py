#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from typing import Callable, List, Tuple, Union


Number = Union[int, float]


class Point:
    def __init__(self, x: Number, y: Number):
        self.__x: Number = x
        self.__y: Number = y

    def __str__(self) -> str:
        return "Point({0}, {1})".format(self.__x, self.__y)

    def __repr__(self) -> str:
        return self.__str__()

    def get_x(self) -> Number:
        return self.__x

    def get_y(self) -> Number:
        return self.__y

    def get_xy(self) -> Tuple[Number, Number]:
        return (self.get_x(), self.get_y())

    def get_distance(self, other: 'Point') -> float:
        x2: float = math.pow(self.get_x() - other.get_x(), 2)
        y2: float = math.pow(self.get_y() - other.get_y(), 2)
        return math.sqrt(x2 + y2)


class Circle:
    def __init__(self, center: Point, radius: Number, check_input = True):
        if check_input and radius <= 0:
            raise ValueError("Radius must be >= 0.")
        self.__center: Point = center
        self.__radius: Number = radius

    def __str__(self) -> str:
        return "Circle(c={0}, r={1})".format(self.__center, self.__radius)

    def __repr__(self) -> str:
        return self.__str__()

    def get_center(self) -> Point:
        return self.__center

    def get_radius(self) -> Number:
        return self.__radius

    def get_dist_betw_centers(self, other: 'Circle') -> float:
        return self.get_center().get_distance(other.get_center())

    def is_other_circle_completely_in_me(self, other: 'Circle',
                                         precision: int = 3) -> bool:
        the_sum: float = self.get_dist_betw_centers(other) + other.get_radius()
        return (round(the_sum, precision) <= round(self.get_radius(), precision))

    def do_circumferences_intersect(self, other: 'Circle',
                                    precision: int = 3) -> bool:
        r1: float = self.get_radius()
        r2: float = other.get_radius()
        dc: float = self.get_dist_betw_centers(other)
        if round(r1, precision) < round(r2, precision):
            return round(dc+r1, precision) > round(r2, precision)
        else:
            return round(dc+r2, precision) > round(r1, precision)


def print_program_description() -> None:
    print("Hi, this is a toy program.")
    print("It determines details of circle geometry.")
    print("NO GUARANTEE THAT THIS PROGRAM WORKS CORRECTLY.")
    print("USE IT AT YOUR OWN RISK.")
    _ = input("Press Enter to continue.")


def print_examples(examples: List[Tuple[Circle, Circle]],
                   expected_answers: List[bool],
                   main_msg: str,
                   every_turn_msg_fn: Callable[[Circle, Circle], str],
                   every_turn_action_fn: Callable[[Circle, Circle], str]
                   ) -> None:
    if len(examples) != len(expected_answers):
        raise ValueError("len(examples) must be equal to len(expected_answers)")
    print(main_msg)
    for i in range(len(examples)):
        circ1, circ2 = examples[i]
        print("-" * 3)
        print(every_turn_msg_fn(circ1, circ2))
        print("Computed answer: {0}".format(every_turn_action_fn(circ1, circ2)))
        print("Expected answer: {0}".format(expected_answers[i]))


def print_examples1() -> None:
    circles1: List[Tuple[Circle, Circle]] = [
        (Circle(Point(7, 6), 4), Circle(Point(6, 7), 1)),
        (Circle(Point(7, 6), 4), Circle(Point(9, 3), 1)),
        (Circle(Point(6, 7), 1), Circle(Point(7, 6), 4))
    ]
    expected_answers1: List[bool] = [True, False, False]
    print_examples(
        circles1, expected_answers1,
        "\nCircle inside circle examples.",
        lambda c1, c2: "Is {0} completely inside {1}?".format(c2, c1),
        lambda c1, c2: str(c1.is_other_circle_completely_in_me(c2)))


def print_examples2() -> None:
    circles2: List[Tuple[Circle, Circle]] = [
        (Circle(Point(7, 6), 4), Circle(Point(9, 8), 2)),
        (Circle(Point(7, 6), 4), Circle(Point(6, 7), 1)),
    ]
    expected_answers2: List[bool] = [True, False]
    print_examples(
        circles2, expected_answers2,
        "\nCircles circumferences intersecion examples.",
        lambda c1, c2: "Do ciurcumferences of {0} and {1} intersect?".format(c1, c2),
        lambda c1, c2: str(c1.do_circumferences_intersect(c2)))


def main() -> None:
    print_program_description()
    print_examples1()
    print_examples2()
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
