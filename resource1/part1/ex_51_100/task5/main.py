# -*- coding: utf-8 -*-

from typing import List


def concatenate_n_strings(*strings: str, sep=" ") -> str:
    return sep.join(strings)


def print_program_description() -> None:
    print("\nHi.")
    print("This is a toy program that concatenates strings.")
    print("NO GUARANTEE THE PROGRAM WORKS CORRECTLY. Use it at Your own risk.")
    print("Ready? Let's begin.")
    _: str = input("Press any key [and then Enter] to continue. ")
    print()


def main() -> None:
    print_program_description()
    exemplary_strings: List[List[str]] = [
        ["Ala"],
        ["Ala", "ma"],
        ["Ala", "ma", "kota"],
        ["Ala", "ma", "kota", "a", "Tomek"],
        ["Ala", "ma", "kota", "a", "Tomek", "ma"],
        ["Ala", "ma", "kota", "a", "Tomek", "ma", "psa"],
    ]
    print("Examples. Strings concatenation")

    for example in exemplary_strings:
        print("-" * 3)
        print("Concatenating {0} with space as a separator.".format(example))
        print("Result: {0}".format(concatenate_n_strings(*example)))

    print()

    for example in exemplary_strings:
        print("-" * 3)
        print("Concatenating {0} with hypen as a separator.".format(example))
        print("Result: {0}".format(concatenate_n_strings(*example, sep="-")))

    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
