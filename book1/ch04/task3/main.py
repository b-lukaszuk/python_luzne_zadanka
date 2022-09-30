# -*- coding: utf-8 -*-

import string


def is_any_letter_of_text_present_in_src(
    text: str, src: str = string.ascii_lowercase
) -> bool:
    return len(set(text).intersection(src)) >= 1


def is_good_password(password: str) -> bool:
    return (
        is_any_letter_of_text_present_in_src(password, string.ascii_lowercase)
        and is_any_letter_of_text_present_in_src(password, string.ascii_uppercase)
        and is_any_letter_of_text_present_in_src(password, string.digits)
        and (len(password) >= 8)
    )


def get_password_candidate_from_user() -> str:
    input_str: str = ""
    input_str = input("\nEnter a candidate for password: ")
    return input_str


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program asks the user to type a password candidate.")
    print("Next it determines is the input a good password.")
    print("Here are some arbitrary assumptions for good passwords.")
    print(
        "Good passwords are >= 8 characters long, contain >= 1 small letter, >= 1 capital letter, >= 1 digit."
    )
    print("The result is printed to the terminal.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    end_program: bool = False
    print_program_description()
    while not end_program:
        password_candidate: str = get_password_candidate_from_user()
        print("Validating input.")
        print("Is it a good password? {0}".format(is_good_password(password_candidate)))
        end_program = input("\nWanna try again [y/n or anything else]? ") not in [
            "y",
            "Y",
        ]
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
