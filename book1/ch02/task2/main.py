# -*- coding: utf-8 -*-

import string
from typing import Tuple


def is_row_in_range(row_number: int) -> bool:
    return row_number > 0 and row_number < 9


def is_column_in_range(column_letter: str) -> bool:
    return (
        column_letter in string.ascii_lowercase[:8]
        or column_letter in string.ascii_uppercase[:8]
    )


# column_letter: str a-h
def is_1st_field_in_column_white(column_letter: str) -> bool:
    no_of_togglings: int = string.ascii_lowercase[:8].index(
        column_letter.lower()
    )
    if no_of_togglings % 2 == 0:
        return False
    else:
        return True


# column_letter: str a-h, row_number: int 1-8
def is_field_white(column_letter: str, row_number: int) -> bool:
    is_1st_field_in_this_row_white: bool = is_1st_field_in_column_white(
        column_letter
    )
    if (row_number - 1) % 2 == 0:
        return is_1st_field_in_this_row_white
    else:
        return not is_1st_field_in_this_row_white


def get_user_input(
    default_column: str = "a", default_row: int = 1
) -> Tuple[str, int]:
    input_column: str = input("enter column name (single letter: a to h): ")
    if not is_column_in_range(input_column):
        print("Invalid input. I default to {0}.\n".format(default_column))
        input_column = default_column
    input_row: str = input("enter row number (integer 1 to 8): ")
    try:
        row_int: int = int(input_row)
        if not is_row_in_range(row_int):
            raise ValueError
    except ValueError:
        print("Invalid input. I default to {0}.\n".format(default_row))
        row_int = default_row
    return (input_column, row_int)


def print_program_description() -> None:
    print("\nHi.\n")
    print("This program asks user for the coordinates of a chessboard field.")
    print("Next it determines the color of the field.")
    print("The result is printed to the terminal.")
    print("NO GUARANTEE OF CORRECT CONVERSION.")
    print("All clear. Then let's begin.\n")


def main() -> None:

    print_program_description()
    (column_letter, row_number) = get_user_input()
    print(
        "The field: {0}{1} is {2}".format(
            column_letter,
            row_number,
            "white" if is_field_white(column_letter, row_number) else "black",
        )
    )

    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
