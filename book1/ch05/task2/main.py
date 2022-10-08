# -*- coding: utf-8 -*-

from typing import Generator


def are_all_characters_legal(text: str, legal_characters: str = "0123456789") -> bool:
    return all([c in legal_characters for c in text])


# excluding the number itself
def get_positive_divisors(number: int) -> Generator[int, None, None]:
    for i in range(1, number):
        if number % i == 0:
            yield i


def is_perfect_number(number: int) -> bool:
    return sum(get_positive_divisors(number)) == number


def get_perfect_numbers(
    min_incl: int = 1, max_incl: int = 10000
) -> Generator[int, None, None]:
    for i in range(min_incl, max_incl + 1):
        if is_perfect_number(i):
            yield i


def print_perfect_numbers(min_incl: int = 1, max_incl: int = 10000) -> None:
    print("\nPrinting perfect numbers.")
    print("Please be patient. Printing the numbers may take a while.")
    print(
        "Perfect numbers from {0} to {1} (inclusive-inclusive) are:".format(
            min_incl, max_incl
        )
    )
    for perf_num in get_perfect_numbers(min_incl, max_incl):
        print(perf_num)


def get_input_from_user(
    min_allowed_inclusive: int = 1,
    max_allowed_inclusive: int = 1000,
) -> int:
    end_asking_for_input: bool = False
    input_str: str = ""
    while not end_asking_for_input:
        input_str = input(
            "Enter integer from {0} to {1}: ".format(
                min_allowed_inclusive,
                max_allowed_inclusive,
            )
        )
        if not are_all_characters_legal(input_str):
            print("Incorrect characters detected. Try again.")
        elif not (min_allowed_inclusive <= int(input_str) <= max_allowed_inclusive):
            print("Number outside the allowed range. Try again.")
        else:
            end_asking_for_input = True
    return int(input_str)


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program asks the user to enter a number.")
    print("Next, it checks if it is a so called perfect number.")
    print("Additionally, it prints all the perfect numbers from a certain range.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()
    number: int = get_input_from_user()
    print("\nIs {0} a perfect number? {1}".format(number, is_perfect_number(number)))
    print_perfect_numbers()
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
