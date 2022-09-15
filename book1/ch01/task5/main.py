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


def get_input_from_user(default_on_error: float = 3) -> List[float]:
    messages: List[str] = [
        "Enter the length [cm] (real number) of a side of a regular polygon: ",
        "Enter the number of sides (integer) of a regular polygon: ",
    ]
    input_s_n: List[float] = [default_on_error, default_on_error]
    for i in range(len(messages)):
        user_input_str: str = input(messages[i])
        try:
            input_s_n[i] = float(user_input_str)
            if not isNumBetween(input_s_n[i], 0.1, 100):
                raise ValueError
        except ValueError:
            print("Invalid input. I default to {0}".format(default_on_error))
            input_s_n[i] = default_on_error
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
        "Calculating the area of a regular polygon with s = {s:.2f} [cm] and n = {n}.".format(
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
