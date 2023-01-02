#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys
from typing import List, Tuple, Union


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

    def is_other_circle_completely_in_me(self, other: 'Circle',
                                         precision: int = 3) -> bool:
        dc: float = self.get_center().get_distance(other.get_center())
        return (round(dc + other.get_radius(), precision) <=
                round(self.get_radius(), precision))


def print_program_description() -> None:
    print("Hi, this is a toy program.")
    print("It determines details of circle geometry.")
    print("NO GUARANTEE THAT THIS PROGRAM WORKS CORRECTLY.")
    print("USE IT AT YOUR OWN RISK.")
    _ = input("Press Enter to continue.")


def print_examples_circle_in_circle(examples: List[Tuple[Circle, Circle]],
                                    expected_answers: List[bool]) -> None:
    if len(examples) != len(expected_answers):
        raise ValueError("len(examples) must be equal to len(expected_answers)")
    print("\nCircle inside circle examples.")
    for i in range(len(examples)):
        circ1, circ2 = examples[i]
        print("-" * 3)
        print("Is {0} completly inside {1}?".format(circ2, circ1))
        print("Computed answer: {0}".format(
            circ1.is_other_circle_completely_in_me(circ2)))
        print("Expected answer: {0}".format(expected_answers[i]))


def main() -> None:
    print_program_description()
    circles1: List[Tuple[Circle, Circle]] = [
        (Circle(Point(7, 6), 4), Circle(Point(6, 7), 1)),
        (Circle(Point(7, 6), 4), Circle(Point(9, 3), 1)),
        (Circle(Point(6, 7), 1), Circle(Point(7, 6), 4))
    ]
    expected_answers1: List[bool] = [True, False, False]
    print_examples_circle_in_circle(circles1, expected_answers1)
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
