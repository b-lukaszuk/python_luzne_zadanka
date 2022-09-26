# -*- coding: utf-8 -*-


def get_number_from_user(
    default_number_on_error: int = 64, minIncl: int = 2, maxIncl: int = 900
) -> int:
    input_str: str = ""
    result: int = default_number_on_error
    input_str = input(
        "\nEnter a number (integer from {0} to {1}): ".format(minIncl, maxIncl)
    )
    try:
        result = int(input_str)
        if result < minIncl or result > maxIncl:
            raise ValueError
    except ValueError:
        print("Invalid input. I default to {0}".format(default_number_on_error))
        result = default_number_on_error
    return result


def is_guess_good_enough(
    guess: float, expected_guess_squared: float, difference: float = 1e-12
) -> bool:
    return abs((guess * guess) - expected_guess_squared) <= difference


def get_updated_guess(prev_guess: float, expected_guess_squared: float) -> float:
    return (prev_guess + expected_guess_squared / prev_guess) / 2


def get_square_root(number: float) -> float:
    guess: float = number / 2
    while not is_guess_good_enough(guess, number):
        guess = get_updated_guess(guess, number)
    return guess


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program computes square root of a number entered by the user.")
    print("It does so by using so called Newton's method.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    end_program: bool = False
    print_program_description()
    while not end_program:
        number: int = get_number_from_user()
        print(
            "The square root of {0} is {1:.4f}.".format(number, get_square_root(number))
        )
        end_program = input("\nWanna try again [y/n or anything else]? ") not in [
            "y",
            "Y",
        ]
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
