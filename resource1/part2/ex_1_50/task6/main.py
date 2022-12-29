#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from typing import Tuple, Union

# https://www.baeldung.com/cs/check-if-point-is-in-2d-triangle

Number = Union[int, float]

class Point:
    def __init__(self, x: Number, y: Number):
        self.__x: Number = x
        self.__y: Number = y

    def __str__(self) -> str:
        return "Point({0}, {1})".format(self.__x, self.__y)

    def __repr__(self) -> str:
        return self.__str__()

    def get_distance(self, other: 'Point') -> float:
        x2: float = math.pow(self.__x - other.__x, 2)
        y2: float = math.pow(self.__y - other.__y, 2)
        return math.sqrt(x2 + y2)


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        if not self.__is_valid_triangle(p1, p2, p3):
            raise ValueError("Incompatible side lenghts to build a triangle.")
        self.__p1: Point = p1
        self.__p2: Point = p2
        self.__p3: Point = p3

    def __str__(self) -> str:
        return "Triangle({0}, {1}, {2})".format(self.__p1, self.__p2, self.__p3)

    def __repr__(self) -> str:
        return self.__str__()

    def __get_side_lengths(
            self, p1: Point, p2: Point, p3: Point) -> Tuple[float, float, float]:
        s1: float = p1.get_distance(p2)
        s2: float = p1.get_distance(p3)
        s3: float = p2.get_distance(p3)
        return (s1, s2, s3)

    def __is_valid_triangle(self, p1: Point, p2: Point, p3: Point) -> bool:
        s1, s2, s3 = self.__get_side_lengths(p1, p2, p3)
        if (s1 + s2) <= s3:
            return False
        if (s1 + s3) <= s2:
            return False
        if (s2 + s3) <= s1:
            return False
        return True


def print_program_description() -> None:
    print("Hi, this is a toy program.")
    print("It determines if a point is inside a triangle.")
    print("NO GUARANTEE THAT THIS PROGRAM WORKS CORRECTLY.")
    print("USE IT AT YOUR OWN RISK.")
    _ = input("Press Enter to continue.")
    print()


def main() -> None:
    print("Examples:")
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
