# -*- coding: utf-8 -*-

from typing import List


def get_greatest_common_divisor_of_m_and_n(m: int, n: int) -> int:
    d: int = min(m, n)
    while not (m % d == 0 and n % d == 0):
        d -= 1
    return d


def get_two_numbers_from_user(
    default_number_on_error: int = 64, minIncl: int = 2, maxIncl: int = 1000
) -> List[int]:
    input_str: str = ""
    results: List[int] = [default_number_on_error, default_number_on_error]
    for i in range(2):
        input_str = input(
            "\nEnter number {0} (integer from {1} to {2}): ".format(
                i + 1, minIncl, maxIncl
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
    print("This is a toy program asks the user for two numbers.")
    print("Next it calculates their greatest common divisor")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    end_program: bool = False
    m, n = [64, 64]
    print_program_description()
    while not end_program:
        m, n = get_two_numbers_from_user()
        print(
            "\nThe greatest common divisor of {0} and {1} is {2}".format(
                m, n, get_greatest_common_divisor_of_m_and_n(m, n)
            )
        )
        end_program = input("\nWanna try again [y/n or anything else]? ") not in [
            "y",
            "Y",
        ]
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
