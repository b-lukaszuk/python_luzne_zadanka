# -*- coding: utf-8 -*-

import math
from typing import List


def get_regular_polygon_area(s: float, n: int) -> float:
    """Returns the area of a regular polygon

    Args:
        s (float): length of a side of polygon [cm squared]
        n (int): number of sides of a polygon

    Returns:
        The area of a regular polygon in cm squared
    """
    return (n * s ** 2) / (4 * math.tan(math.pi / n))


def isNumBetween(num: float, minIncl: float, maxIncl: float) -> bool:
    return (num >= minIncl) and (num <= maxIncl)


def get_input_from_user(
    mins_of_inputs: List[float] = [0.1, 3],
    maxes_of_inputs: List[float] = [1000, 100],
    defaults_on_error: List[float] = [2, 3],
    messages: List[str] = [
        "Enter the length [cm] (real number from: {0} to {1}) of a side of a regular polygon: ",
        "Enter the number of sides (integer from {0} to {1}) of a regular polygon: ",
    ],
) -> List[float]:
    """Returns user's input of side length and number of sides

    Args:
        mins_of_inputs (List[float]) - minimal values of side's length and number of sides
        maxes_of_inputs (List[float]) - maximal values of side's length and number of sides
        defaults_on_error (List[float]) - default values to return for side's length and number of sides if the input is wrong
        messages (List[str]) - prompts to display while asking an user for input

    Returns:
        List[float] - length of a side and number of sides
    """
    input_s_n: List[float] = defaults_on_error.copy()
    for i in range(len(messages)):
        user_input_str: str = input(
            messages[i].format(mins_of_inputs[i], maxes_of_inputs[i])
        )
        try:
            input_s_n[i] = float(user_input_str)
            if not isNumBetween(input_s_n[i], mins_of_inputs[i], maxes_of_inputs[i]):
                raise ValueError
        except ValueError:
            print("Invalid input. I default to {0}".format(defaults_on_error[i]))
            input_s_n[i] = defaults_on_error[i]
    return input_s_n


def print_program_description() -> None:
    print("\nHi.\n")
    print("This program calculates the area of a regular polygon.")
    print("To do that it reads the length of its side and the number of its sides.")
    print("The two are provided by the user.")
    print("All clear. Then let's begin.\n")
    print(
        "BTW. NO GUARANTEE OF CORRECT RESULTS. STILL, I HOPE IT WILL WORK JUST FINE.\n"
    )


def main() -> None:
    print_program_description()

    (s, n) = get_input_from_user()
    print(
        "\nCalculating the area of a regular polygon with s = {s:.2f} [cm] and n = {n}.".format(
            s=s, n=math.ceil(n)
        )
    )
    print(
        "Result: {result:.3f} [cm^2].".format(
            result=get_regular_polygon_area(s, math.ceil(n))
        )
    )

    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
