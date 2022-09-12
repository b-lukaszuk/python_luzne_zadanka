# -*- coding: utf-8 -*-

import math
from typing import List, Dict


def get_final_speed(
    distance: float, initial_speed: float = 0, acceleration: float = 9.8
) -> float:
    """Returns the speed of a dropped object [m/s] when it hits the ground

    Args:
        distance (float): distance [meters] from which an object is dropped
        initial_speed (float): initial speed [meters per second] of a falling object
        acceleration (float): acceleration [meters per second squared] of a falling object

    Returns:
        The final speed [meters per second] of a falling object when it hits the ground
    """
    return math.sqrt(initial_speed ** 2 + 2 * acceleration * distance)


def isNumBetween(num: float, minIncl: float, maxIncl: float) -> bool:
    return (num >= minIncl) and (num <= maxIncl)


def get_input_from_user(default_on_error: float = 2) -> float:
    print("Enter the location of the object (meters above the ground) ")
    user_input_str: str = input("The value should be a decimal between 0.1 and 10.0: ")
    try:
        user_input_float: float = float(user_input_str)
        if not isNumBetween(user_input_float, 0.1, 10):
            raise ValueError
        return user_input_float
    except ValueError:
        print("Invalid input. I default to {0}".format(default_on_error))
        return default_on_error


def print_program_description() -> None:
    print("\nHi.\n")
    print("This program reads the height from which an object is dropped (free fall)")
    print("It returns the final speed [m/s] of the object when it hits the ground")
    print("The calculations are based on the formula:")
    print("sqrt(initial_speed^ 2 + 2 * acceleration * height)")
    print("It assumes the acceleration equal to: g = 9.8 [m/s^2]")
    print("NO GUARANTEE OF CORRECT RESULTS. STILL, I HOPE IT WILL WORK JUST FINE")
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()

    initial_height: float = get_input_from_user()
    print("\nCalculating the final speed of the object when it hits the ground")
    print("Result: {:.3f} [m/s]".format(get_final_speed(initial_height)))

    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
