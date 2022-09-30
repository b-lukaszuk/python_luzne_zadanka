# -*- coding: utf-8 -*-

import random


def get_random_char_ascii(
    ascii_position_min: int = 33, ascii_position_max: int = 126
) -> str:
    return chr(random.randint(ascii_position_min, ascii_position_max))


def get_random_password(length_min: int = 7, length_max: int = 10) -> str:
    password_length: int = random.randint(length_min, length_max)
    return "".join([get_random_char_ascii() for _ in range(password_length)])


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program that generates a passwords.")
    print("The password is of random length (7-10 characters long).")
    print(
        "It contains characters from ascii position 33 to 126 (inclusive, inclusive)."
    )
    print("The result is printed to the terminal.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    end_program: bool = False
    print_program_description()
    while not end_program:
        print("\nYour random password is: {0}".format(get_random_password()))
        end_program = input("\nWanna try again [y/n or anything else]? ") not in [
            "y",
            "Y",
        ]
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
