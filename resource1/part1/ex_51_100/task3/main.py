# -*- coding: utf-8 -*-

from typing import List
import random


def sum_digits_in_int(number: int) -> int:
    lst_of_digits: List[int] = [int(str_num) for str_num in list(str(number))]
    return sum(lst_of_digits)


def print_program_description() -> None:
    print("\nHi.")
    print("This is a program that calculates the sum of digits in a number.")
    print("NO GUARANTEE THE PROGRAM WORKS CORRECTLY. Use it at Your own risk.")
    print("Ready? Let's begin.")
    _: str = input("Press any key [and then Enter] to continue. ")
    print()


def main() -> None:
    print_program_description()
    print("Examples. Numbers are drawn at random.")
    random.seed(a=None)
    test_numbers: List[int] = random.choices(population=range(1, 1000), k=5)
    for test_num in test_numbers:
        print("sum({0}) = {1}".format(test_num, sum_digits_in_int(test_num)))
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
