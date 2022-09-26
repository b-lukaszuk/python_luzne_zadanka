# -*- coding: utf-8 -*-

import string


def is_letter_in_lowercase_alphabet(letter: str) -> bool:
    return letter in string.ascii_lowercase


def remove_non_alphabet_letters(text: str) -> str:
    return "".join(list(filter(lambda x: is_letter_in_lowercase_alphabet(x), text)))


def is_multiple_words_palindrome(text: str) -> bool:
    only_alphabet_leters: str = remove_non_alphabet_letters(text.lower())
    return only_alphabet_leters == only_alphabet_leters[::-1]


def get_string_from_user() -> str:
    input_str: str = input("\nEnter a word/phrase: ")
    return input_str


def print_program_description() -> None:
    print("\nHi.\n")
    print(
        "This is a toy program that checks if the user's input is a multiple words palindrome."
    )
    print("The characters outside the latin alphabet (ascii) are ignored")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    end_program: bool = False
    print_program_description()
    while not end_program:
        text: str = get_string_from_user()
        print(
            "Is <<{0}>> a multipile words palindrome? {1}".format(
                text, is_multiple_words_palindrome(text)
            )
        )
        end_program = input("\nWanna try again [y/n or anything else]? ") not in [
            "y",
            "Y",
        ]
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
