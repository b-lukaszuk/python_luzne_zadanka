# -*- coding: utf-8 -*-

from typing import List


def get_greatest_common_divisor_of_m_and_n(m: int, n: int) -> int:
    d: int = min(m, n)
    while not (m % d == 0 and n % d == 0):
        d -= 1
    return d


def get_reduced_fraction(numerator: int, denominator: int) -> List[int]:
    greatest_common_divisor: int = get_greatest_common_divisor_of_m_and_n(
        numerator, denominator
    )
    return [
        int(numerator / greatest_common_divisor),
        int(denominator / greatest_common_divisor),
    ]


def get_input_from_user(
    default_on_error: int = 5,
    min_allowed_inclusive: int = 1,
    max_allowed_inclusive: int = 1000,
) -> List[int]:
    names_of_inputs: List[str] = [
        "nominator",
        "denominator",
    ]
    results: List[int] = [default_on_error] * 2
    for i in range(len(names_of_inputs)):
        input_str = input(
            "Enter {0} (integer from {1} to {2}): ".format(
                names_of_inputs[i],
                min_allowed_inclusive,
                max_allowed_inclusive,
            )
        )
        try:
            results[i] = int(input_str)
            if not (min_allowed_inclusive <= results[i] <= max_allowed_inclusive):
                raise ValueError
        except ValueError:
            print("Invalid input. I default to {0}".format(default_on_error))
            results[i] = default_on_error
    return results


def declare_conversion(numerator: int, denominator: int) -> None:
    numerator2, denominator2 = get_reduced_fraction(numerator, denominator)
    print("{0}\t \t{1}".format(numerator, numerator2))
    print("----\t=\t----")
    print("{0}\t \t{1}".format(denominator, denominator2))


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program asks the user to enter a fraction.")
    print("Next, the program reduces it to smaller fraction (if possible).")
    print("The result is printed to the terminal.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    end_program: bool = False
    print_program_description()
    while not end_program:
        print()
        numerator, denominator = get_input_from_user()
        declare_conversion(numerator, denominator)
        end_program = input("\nWanna try again [y/n or anything else]? ") not in [
            "y",
            "Y",
        ]
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
