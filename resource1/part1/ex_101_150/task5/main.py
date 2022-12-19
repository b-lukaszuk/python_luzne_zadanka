# -*- coding: utf-8 -*-

from typing import List


def are_all_chars_OK(text_to_test: str, legal_chars: str = "01") -> bool:
    return all([ch in legal_chars for ch in text_to_test])


# groups string by the same chars, from left to right
def group_by_same_chars(text: str) -> List[str]:
    result: List[str] = [""] if text.strip() == "" else [text[0]]
    for i in range(1, len(text)):
        if text[i] == result[-1][0]:
            result[-1] += text[i]
        else:
            result.append(text[i])
    return result


def are_all_pair_of_strings_the_same_lenghts(strings: List[str]) -> bool:
    lengths: List[int] = [len(s) for s in strings]
    for i in range(0, len(strings), 2):
        if lengths[i] != lengths[i + 1]:
            return False
    return True


def are_zeros_followed_by_ones(text: str) -> bool:
    if not are_all_chars_OK(text, "01"):
        raise ValueError("Illegal characters (not 0 or 1) detected.")
    zeros_ones_grouped: List[str] = group_by_same_chars(text.lstrip("1"))
    if len(zeros_ones_grouped) % 2 == 1:
        return False
    return are_all_pair_of_strings_the_same_lenghts(zeros_ones_grouped)


def print_program_description() -> None:
    print("\nHi.")
    print("This is a toy program.")
    print("It tests a random string to see")
    print("if every consecutive sequence of zeroes is followed")
    print("by a consecutive sequence of ones of same length.")
    print("NO GUARANTEE THE PROGRAM WORKS CORRECTLY. Use it at Your own risk.")
    print("Ready? Let's begin.")
    _: str = input("Press any key [and then Enter] to continue. ")
    print()


def main() -> None:
    print_program_description()
    tested_strings: List[str] = [
        "01010101",
        "00",
        "000111000111",
        "00011100011",
        "11000111000111",
        "111111",
    ]
    expected_results: List[bool] = [True, False, True, False, True, False]
    for i in range(len(tested_strings)):
        print("-" * 3)
        print("Testing input: {0}".format(tested_strings[i]))
        print("Are 0s followed by equal num of 1s?")
        print(
            "Result of testing: {0}.".format(
                are_zeros_followed_by_ones(tested_strings[i])
            )
        )
        print("Expected result {0}.".format(expected_results[i]))
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
