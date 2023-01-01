#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

    def __eq__(self, other: 'Point') -> bool:
        return (self.__x == other.__x) and (self.__y == other.__y)

    def __ne__(self, other: 'Point') -> bool:
        return not self.__eq__(other)

    def get_x(self) -> Number:
        return self.__x

    def get_y(self) -> Number:
        return self.__y

    def get_xy(self) -> Tuple[Number, Number]:
        return (self.get_x(), self.get_y())


class Line:
    def __init__(self, p1: Point, p2: Point, check_input = True):
        if check_input and p1 == p2:
            raise ValueError("p1 == p2, so it is a Point not a line.")
        self.__p1: Point = p1
        self.__p2: Point = p2

    def __str__(self) -> str:
        return "Line({0}, {1})".format(self.__p1, self.__p2)

    def __repr__(self) -> str:
        return self.__str__()

    def get_slope(self) -> float:
        x1, y1 = self.__p1.get_xy()
        x2, y2 = self.__p2.get_xy()
        xs = [x1, x2]
        ys = [y1, y2]
        numerator: float = sum([x1*y1, x2*y2]) - (sum(xs) * sum(ys) / 2)
        denominator: float = sum([x**2 for x in xs]) - ((sum(xs)**2) / 2)
        # denominator == 0 for straight vertical line
        return numerator / denominator if denominator != 0 else sys.maxsize

    def is_parallel(self, other: 'Line', precision: int = 3) -> bool:
        s1: float = round(self.get_slope(), precision)
        s2: float = round(other.get_slope(), precision)
        return  s1 == s2


def print_program_description() -> None:
    print("Hi, this is a toy program.")
    print("It determines if two lines are parallel.")
    print("NO GUARANTEE THAT THIS PROGRAM WORKS CORRECTLY.")
    print("USE IT AT YOUR OWN RISK.")
    _ = input("Press Enter to continue.")
    print()


def print_examples(lines: List[Tuple[Line, Line]], expected_answers: List[bool]) -> None:
    print("Examples:")
    print("Precision of estimate 3 decimal places.")
    for i in range(len(lines)):
        l1, l2 = lines[i]
        print("-" * 3)
        print("Is {0} parallel to {1}?".format(l1, l2))
        print("Result of determination: {0}".format(l1.is_parallel(l2)))
        print("Expected answer: {0}".format(expected_answers[i]))


def main() -> None:
    lines: List[Tuple[Line, Line]] = [
        (Line(Point(2, 5), Point(6, 4)), Line(Point(8, 3), Point(9, 7))),
        (Line(Point(2, 5), Point(6, 5)), Line(Point(4, 10), Point(8, 10))),
        (Line(Point(2, 5), Point(2, 10)), Line(Point(4, 6), Point(4, 11))),
        (Line(Point(2, 7), Point(6, 7)), Line(Point(4, 5), Point(4, 10))),
        (Line(Point(7, 4), Point(11, 7)), Line(Point(7, 7), Point(11, 4))),
        (Line(Point(2, 4), Point(4, 2)), Line(Point(4, 4), Point(6, 2)))
    ]
    expected_answers: List[bool] = [False, True, True, False, False, True]
    print_program_description()
    print_examples(lines, expected_answers)
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
