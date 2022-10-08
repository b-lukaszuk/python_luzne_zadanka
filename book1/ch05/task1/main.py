# -*- coding: utf-8 -*-

from typing import List


def are_all_characters_legal(text: str, legal_characters: str = "+-0123456789") -> bool:
    return all([c in legal_characters for c in text])


def get_input_from_user(
    min_allowed_inclusive: int = -100,
    max_allowed_inclusive: int = 100,
) -> List[int]:
    results: List[int] = []
    end_input: bool = False
    counter: int = 1
    while not end_input:
        print(
            "\nEnter number (integer between {0} and {1}) and press Enter.".format(
                min_allowed_inclusive, max_allowed_inclusive
            )
        )
        print("Blank line (just Enter with no number) ends the input series.")
        input_str = input("Your input (id: {0}): ".format(counter)).strip()
        if input_str == "":
            print("Blank line detected. End of input.")
            end_input = True
        elif not are_all_characters_legal(input_str):
            print("Illegal characters detected, no number added to list of inputs.")
        elif not (min_allowed_inclusive <= int(input_str) <= max_allowed_inclusive):
            print("Number outside of range, no number added to list of inputs.")
        else:
            counter += 1
            results.append(int(input_str))
    return results


def print_list(numbers: List[int]) -> None:
    for number in numbers:
        print(number, end=", ")


def print_sorted_input(numbers: List[int]) -> None:
    negatives: List[int] = [num for num in numbers if num < 0]
    zeros: List[int] = [num for num in numbers if num == 0]
    positives: List[int] = [num for num in numbers if num > 0]
    for sub_list in [negatives, zeros, positives]:
        print_list(sub_list)
    print("\b\b")


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program asks the user to enter a number.")
    print("Then it asks You for another number, and another.")
    print("To finish type blank line (press Enter without any other input).")
    print("Then the program displays:")
    print("1) all negative numbers, all zeros, all positive numbers.")
    print("Within the group the numbers are displayed in order they were entered.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.\n")


def main() -> None:
    print_program_description()
    numbers: List[int] = get_input_from_user()
    print(
        "\nYour numbers sorted by categories (negatives, zeros, positives) are (empty line if no numbers were entered):"
    )
    print_sorted_input(numbers)
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
