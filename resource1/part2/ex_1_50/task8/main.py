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

    def get_x(self) -> Number:
        return self.__x

    def get_y(self) -> Number:
        return self.__y

    def get_xy(self) -> Tuple[Number, Number]:
        return (self.get_x(), self.get_y())


class Circle:
    def __init__(self, center: Point, radius: float, check_input = True):
        if check_input and radius <= 0:
            raise ValueError("Radius must be >= 0.")
        self.__center: Point = center
        self.__radius: float = radius

    def __str__(self) -> str:
        return "Circle(c={0}, r={1})".format(self.__center, self.__radius)

    def __repr__(self) -> str:
        return self.__str__()


def print_program_description() -> None:
    print("Hi, this is a toy program.")
    print("It determines if two lines are parallel.")
    print("NO GUARANTEE THAT THIS PROGRAM WORKS CORRECTLY.")
    print("USE IT AT YOUR OWN RISK.")
    _ = input("Press Enter to continue.")
    print()


def main() -> None:
    print_program_description()
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
