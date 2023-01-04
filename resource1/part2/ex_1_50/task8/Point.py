#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from Number import Number
from typing import Tuple


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
