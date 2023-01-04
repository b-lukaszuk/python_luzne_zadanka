#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Number import Number
from Point import Point


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

    def does_it_overlap(self, other: 'Circle', precision: int = 3) -> bool:
        dc: float = self.get_dist_betw_centers(other)
        sum_rs: float = self.get_radius() + other.get_radius()
        return round(dc, precision) < round(sum_rs, precision)
