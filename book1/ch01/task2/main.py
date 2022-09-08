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


class LongPoint(TypedDict):
    latitude: Latitude
    longitude: Longitude


class ShortPoint(TypedDict):
    latitude: int
    longitude: int


exemplary_point: LongPoint = {
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


def handleUserInput(exemplary_point: LongPoint = exemplary_point) -> ShortPoint:
    user_input_str: str = ""
    user_input_int: int = 0
    result: ShortPoint = {"latitude": 0, "longitude": 0}
    for key in exemplary_point.keys():
        user_input_str = input(
            "Enter the value for {0} and press enter: ".format(
                exemplary_point[key]["message"]
            )
        )
        try:
            user_input_int: int = int(user_input_str)
            if isNumBetween(
                user_input_int,
                exemplary_point[key]["minIncl"],
                exemplary_point[key]["maxIncl"],
            ):
                result[key] = user_input_int
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. I default to 0\n")
    return result


def getNPointsFromUser(how_many: int = 2) -> List[ShortPoint]:
    points: List[ShortPoint] = []
    for _ in range(how_many):
        points.append(handleUserInput())
    return points


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
    twoPoints: List[ShortPoint] = getNPointsFromUser()
    print("points: ", twoPoints)
    print("That's all. Goodbye!")


if __name__ == "__main__":
    main()
