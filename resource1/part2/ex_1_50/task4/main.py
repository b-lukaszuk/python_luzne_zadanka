#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from typing import Set


def all_chars_nums(text: str) -> bool:
    return all([ch in "0123456789" for ch in text])


def get_missing_numbers(tel_num: str) -> str:
    if not all_chars_nums(tel_num):
        raise ValueError("All characters must be numbers.")
    all_nums: Set[str] = set(list("0123456789"))
    nums_present: Set[str] = set(list(tel_num))
    missing_nums: Set[str] = all_nums - nums_present
    return "".join(sorted(list(missing_nums)))


def get_random_tel_num() -> str:
    return "".join(random.choices(population=list("0123456789"), k=9))


def print_program_description() -> None:
    print("Hi, this is a toy program.")
    print("It investigates a (phone) number and determines missing numbers.")
    print("NO GUARANTEE THAT THIS PROGRAM WORKS CORRECTLY.")
    print("USE IT AT YOUR OWN RISK.")
    _ = input("Press Enter to continue.")
    print()


def main() -> None:
    phone_num: str = ""
    print_program_description()
    print("Examples:")
    for _ in range(5):
        phone_num = get_random_tel_num()
        print("-" * 3)
        print(
            "Missing numbers in {0} are: {1}".format(
                phone_num, get_missing_numbers(phone_num)
            )
        )
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
