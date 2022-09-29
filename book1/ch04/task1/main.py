# -*- coding: utf-8 -*-

import string
from typing import List


def declare_test_for_building_triangle(side_a: int, side_b: int, side_c: int) -> None:
    if side_b + side_c <= side_a:
        print("No, length side A >= sum(length side B, length side C).")
    elif side_a + side_c <= side_b:
        print("No, length side B >= sum(length side A, length side C).")
    elif side_a + side_b <= side_c:
        print("No, length side C >= sum(length side A, length side B).")
    else:
        print("Yes, you can create a triangle with the three sides.")


def get_n_numbers_from_user(
    n: int = 3, default_number_on_error: int = 10, minIncl: int = 1, maxIncl: int = 100
) -> List[int]:
    input_str: str = ""
    results: List[int] = [default_number_on_error] * n
    for i in range(n):
        input_str = input(
            "\nEnter the length (in cm) for side {0} (integer from {1} to {2}): ".format(
                string.ascii_lowercase[i], minIncl, maxIncl
            )
        )
        try:
            results[i] = int(input_str)
            if results[i] < minIncl or results[i] > maxIncl:
                raise ValueError
        except ValueError:
            print("Invalid input. I default to {0}".format(default_number_on_error))
            results[i] = default_number_on_error
    return results


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program asks the user for three numbers.")
    print("The numbers are potential candidates for sides of a triangle.")
    print("Next it determines are they suitable for building a triangle.")
    print("The result is printed to the terminal.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    end_program: bool = False
    print_program_description()
    while not end_program:
        a, b, c = get_n_numbers_from_user()
        print("\nCan you create a trianle with the following sides lengths")
        print("Side a: {0} [cm], side b: {1} [cm], side c: {2} [cm]?".format(a, b, c))
        declare_test_for_building_triangle(a, b, c)
        end_program = input("\nWanna try again [y/n or anything else]? ") not in [
            "y",
            "Y",
        ]
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
