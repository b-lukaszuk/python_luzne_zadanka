# -*- coding: utf-8 -*-

import math
from typing import List, TypedDict


class Latitude(TypedDict):
    value: int
    minIncl: int
    maxIncl: int
    message: str


class Longitude(TypedDict):
    value: int
    minIncl: int
    maxIncl: int
    message: str


class Point(TypedDict):
    latitude: Latitude
    longitude: Longitude


exemplary_point: Point = {
    "latitude": {
        "value": 0,
        "minIncl": -90,
        "maxIncl": 90,
        "message": "lattitude in degrees [integer from -90 (south pole) to 90 (north pole)]",
    },
    "longitude": {
        "value": 0,
        "minIncl": -180,
        "maxIncl": 180,
        "message": "longitude in degrees [integer from -180 (westward) to 180 (eastward)]",
    },
}


def isNumBetween(num: int, minIncl: int, maxIncl: int) -> bool:
    return (num >= minIncl) and (num <= maxIncl)


def print_program_description() -> None:
    print("\nHi.\n")
    print(
        "This program reads the position of two points (lattitude and longitude) on the earth's surface."
    )
    print(
        "Next it will perform some calculations and return the distance between the points."
    )
    print("The results of the operation will be printed to the terminal.")
    print(
        "There is no guarantee of correct results (although I hope it will work just fine)"
    )
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()
    print("That's all. Goodbye!")


if __name__ == "__main__":
    main()
