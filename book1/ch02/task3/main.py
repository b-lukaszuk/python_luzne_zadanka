# -*- coding: utf-8 -*-

from typing import List

chinese_zodiac_years_2000_2011: List[str] = [
    "Dragon",
    "Snake",
    "Horse",
    "Sheep",
    "Monkey",
    "Rooster",
    "Dog",
    "Pig",
    "Rat",
    "Ox",
    "Tiger",
    "Hare",
]


def get_chinese_zodiac(
    year: int, signs_for_2000_2011: List[str] = chinese_zodiac_years_2000_2011
) -> str:
    return signs_for_2000_2011[(year - 2000) % 12]


def get_user_input(
    default_year: int = 2002, min_year: int = 1, max_year: int = 5000
) -> int:
    year_str: str = input(
        "Enter the year (integer from {0} to {1}): ".format(min_year, max_year)
    )
    try:
        year_int: int = int(year_str)
        if not (year_int >= min_year and year_int <= max_year):
            raise ValueError
    except ValueError:
        print("Invalid input. I default to {0}.\n".format(default_year))
        year_int = default_year
    return year_int


def print_program_description() -> None:
    print("\nHi.\n")
    print("This program asks user for to enter a year.")
    print("Next it determines the sign of chinese zodiac attributed to it.")
    print("The result is printed to the terminal.")
    print("NO GUARANTEE OF CORRECT RESULT. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def main() -> None:

    print_program_description()
    year: int = get_user_input()
    print(
        "\nIn chinese zodiac the year {0} is a year of the {1}.".format(
            year, get_chinese_zodiac(year)
        )
    )

    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
