# -*- coding: utf-8 -*-

import string


def isPalindrome(word: str) -> bool:
    if len(word) < 2:
        return True
    else:
        return word[0] == word[-1] and isPalindrome(word[1:-1])


def is_letter_in_lowercase_alphabet(letter: str) -> bool:
    return letter in string.ascii_lowercase


def remove_non_alphabet_characters(text: str) -> str:
    return "".join(list(filter(lambda x: is_letter_in_lowercase_alphabet(x), text)))


def is_multiple_words_palindrome(text: str) -> bool:
    only_lowercase_a_to_z: str = remove_non_alphabet_characters(text.lower())
    return isPalindrome(only_lowercase_a_to_z)


def get_string_from_user() -> str:
    input_str: str = input("\nEnter a word/phrase: ")
    return input_str


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program.")
    print("It checks if the user's input is a multiple words palindrome.")
    print("The user input is lowercased.")
    print("Spaces and non ASCII characters are removed.")
    print("The test is performed using resursive function.")
    print("So do not type too long and too tricky strings.")
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
