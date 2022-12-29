#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random
from typing import List, Union


Number = Union[int, float]


def is_odd(num: int) -> bool:
    return num % 2 == 1


def get_median(*nums: List[Number]) -> float:
    nums_asc: List[Number] = sorted(nums)
    len_nums: int = len(nums_asc)
    mid: int = math.floor(len_nums / 2)
    return (nums_asc[mid] if is_odd(len_nums)
            else sum(nums_asc[mid - 1: mid + 1]) / 2)


def get_rand_nums(how_many: int = 5) -> List[int]:
    random.seed(None)
    return random.choices(population=range(-10, 11), k=how_many)


def print_program_description() -> None:
    print("Hi, this is a toy program.")
    print("It calculates the median out of a finite series of numbers.")
    print("NO GUARANTEE THAT THIS PROGRAM WORKS CORRECTLY.")
    print("USE IT AT YOUR OWN RISK.")
    _ = input("Press Enter to continue.")
    print()


def main() -> None:
    nums: List[int] = []
    print_program_description()
    print("Examples:")
    for i in range(1, 6):
        nums = get_rand_nums(i)
        print("-" * 3)
        print("Median of {0} is: {1}".format(nums, get_median(*nums)))
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
